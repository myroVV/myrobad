
#•----------Modules----------•#

import discord

from discord.ext import commands

import aiosqlite 

#•----------Class----------•
class Database(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        #self.bot.db refers to
        #bot.db under connect_db
        #In Maine File
        self.db = self.bot.db
        
#•--------------------------------•
        
#STATEMENTS
#fetchone() : Only used when fetching one row
#fetchmany() : Used when fetching multiple rows
#executescript(): 
#commit() : Save data to database
#close : Close database connection 
  #-{To make sure we don't have a bunch of them open}

#QUERIES
#INTEGER : Digit
#FLOAT : Numbers as floats
#PRIMARY KEY : 
#FOREIGN KEY : 
#NULL : something that is not set
#TEXT : Used for text

#TABLES STATEMENTS
#SELECT : Selecting a column from a table
#SELECT * : Select all columns
#INSERT INTO : Inserting new data into a column
#DELETE FROM : Deleting data from a column
#DISTINCT :

#•----------Functions----------•#
    
    #Used to close the database connection
    async def close(self):
      
        return await self.db.close()
        
    #Used to commit (save) changes to database
    async def commit(self):
      
        return await self.db.commit()
    
    #Used to get database cursor
    #execute returns a cursor
    async def execute(self, sql, *param):
      
        return await self.db.execute(sql, param)
        
#•----------------Guilds----------------•#
    
    #Function used to add a new guild
    #To the guilds table
    async def add_guild(self, gid):
      
        result = await self.execute("INSERT OR IGNORE INTO guilds(id) VALUES(?)", gid)
        
        await self.commit()
        return result
        
#•----------Welcome/Goodbye System----------•%
        
    #Function to set welcome channel
    async def welcome_channel(self, gid, cid):
      
        result = await (await self.execute("SELECT channel_id FROM welcome WHERE guild_id = ?", gid)).fetchone()
        
        if result is None:
            await self.execute("INSERT INTO welcome(guild_id, channel_id) VALUES(?, ?)", gid, cid)
            
        elif result is not None:
            await self.execute("UPDATE welcome SET channel_id = ? WHERE guild_id = ?", cid, gid)
            
        await self.commit()
        
        return result
        #await self.close()
        
    #Function to set goodbye channel
    async def goodbye_channel(self, gid, cid):
        
        result = await (await self.execute("SELECT channel_id FROM goodbye WHERE guild_id = ?", gid)).fetchone()
        
        if result is None:
            await self.execute("INSERT INTO goodbye(guild_id, channel_id) VALUES(?, ?)", gid, cid)
        elif result is not None:
            await self.execute("UPDATE goodbye SET channel_id = ? WHERE guild_id = ?", cid, gid)
            
        await self.commit()
        
        return result
        
    #Function to set welcome text
    async def welcome_text(self, gid, w_text):
        
        result = await (await self.execute("SELECT msg FROM welcome WHERE guild_id = ?", gid)).fetchone()
        
        if result is None:
            await self.execute("INSERT INTO welcome(guild_id, msg) VALUES(?, ?)", gid, w_text)
            
        elif result is not None:
            await self.execute("UPDATE welcome SET msg = ? WHERE guild_id = ?", w_text, gid)
            
        await self.commit()
        
        return result
        #await self.close()
    
    #Function to set goodbye text
    async def goodbye_text(self, gid, g_text):
        
        result = await (await self.execute("SELECT msg FROM goodbye WHERE guild_id = ?", gid)).fetchone()
        
        if result is None:
            await self.execute("INSERT INTO goodbye(guild_id, msg) VALUES(?, ?)", gid, g_text)
        
        elif result is not None:
            await self.execute("UPDATE goodbye SET msg = ? WHERE guild_id = ?", g_text, gid)
            
        await self.commit()
        
        return result
        
    #Function to get the current
    #Welcome channel
    async def get_welcome_channel(self, gid):
        
        result = await (await self.execute("SELECT channel_id FROM welcome WHERE guild_id = ?", gid)).fetchone()
        
        return result
        
    #Function to get the current
    #Goodbye channel
    async def get_goodbye_channel(self, gid):
      
        result = await (await self.execute("SELECT channel_id FROM goodbye WHERE guild_id = ?", gid)).fetchone()

        return result
        
    #Function to get the set welcome message
    async def get_w_text(self, gid):
        
        result = await (await self.execute("SELECT msg FROM welcome WHERE guild_id = ?", gid)).fetchone()

        return result[0]
        
    #Function to get the set goodbye message
    async def get_g_text(self, gid):
        
        result = await (await self.execute("SELECT msg FROM goodbye WHERE guild_id = ?", gid)).fetchone()

        return result[0]
        
    #Function to remove the welcome channel
    async def remove_w_channel(self, gid):
      
        result = await self.execute("UPDATE welcome SET channel_id = NULL WHERE guild_id = ?", gid)
        
        await self.commit()
        
        return result
        
    #Function to remove the goodbye channel
    async def remove_g_channel(self, gid):
        
        result = await self.execute("UPDATE goodbye SET channel_id = NULL WHERE guild_id = ?", gid)
        
        await self.commit()
        
        return result
        
    #Function to delete set welcome message
    async def remove_w_text(self, gid):
      
        #Set the column to null
        #From the database
        result = await self.execute("UPDATE welcome SET msg = NULL WHERE guild_id = ?", gid)
        print(result)

        await self.commit()
        
        return result
        
    #Function to delete set goodbye message
    async def remove_g_text(self, gid):
        
        #Delete the set message from database
        #From the database
        result = await self.execute("UPDATE goodbye SET msg = NULL WHERE guild_id = ?", gid)
        print(result)
        
        await self.commit()
        
        return result
        
#•----------Warn System-----------•#
    
    #Function used to add warns
    #To a user
    async def add_warns(self, uid, modid, rsn, gid):
        
        result = await self.execute("INSERT OR IGNORE INTO warns(user_id, mod_id, reason, guild_id) VALUES(?, ?, ?, ?)", uid, modid, rsn, gid)
        
        await self.commit()
        
        return result
    
    #Function user to get all of a user's warns
    async def get_warns(self, uid, gid):
        
        result = await (await self.execute("SELECT * FROM warns WHERE user_id = ? AND guild_id = ?", uid, gid)).fetchall()

        return result

    #Function to delete a user's specific warn
    async def delete_warn(self, warnid):
        
        result = await self.execute("DELETE FROM warns WHERE warn_id = ?", warnid)
        print(result)
        
        await self.commit()
        
        return result

    #Function used to clear all of a user's warns
    async def clear_warns(self, uid, gid):
      
        result = await self.execute("DELETE FROM warns WHERE user_id = ? AND guild_id = ?", uid, gid)
        
        await self.commit()
        
        return result
        
#•----------Mute/Unmute System----------•#
    
    #Function used to add the mute to a member
    async def add_mute(self, mid, rid, endt, gid):
        
        result = await self.execute("INSERT INTO mutes(user_id, role_id, end_time, guild_id) VALUES (?, ?, ?, ?)", mid, rid, endt, gid)
        
        await self.commit()
        
        return result

    #Function used to get the member's roles
    async def get_mutes(self, mid, gid):
        
        result = await (await self.execute("SELECT role_id FROM mutes WHERE user_id = ? AND guild_id = ?", mid, gid)).fetchone()
        
        return result
    
    #Function used to unmute the member(s)
    async def un_mute(self, mid):
        
        result = await self.execute("DELETE FROM mutes WHERE user_id = ?", mid)
        
        await self.commit()
        
        return result

#•----------Prefix System----------•#
  
    #Function to get prefix
    async def get_prefix(self, gid):
        
        result = await (await self.execute("SELECT prefixes FROM guilds WHERE id = ?", gid)).fetchone()
        
        return result[0]

    #Function to set the prefix   
    async def set_prefix(self, gid, pre):
  
        result = await (await self.execute("SELECT prefixes FROM guilds WHERE id = ?", gid)).fetchone()
        
        if result is None:
            await self.execute("INSERT INTO guilds(id, prefixes) VALUES(?, ?)", gid, pre)
        elif result is not None:
            await self.execute("UPDATE guilds SET prefixes = ? WHERE id = ?", pre, gid)
        
        await self.commit()

        return result
    
    #Function to delete the custom prefix
    async def drop_prefix(self, gid):
        
        #Set the custom prefix to the default
        result = await self.execute("UPDATE guilds SET prefixes = '?' WHERE id = ?", gid)

        await self.commit()

        return result

def setup(bot):
    bot.add_cog(Database(bot))
