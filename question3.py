import time
import datetime

class PYlruCache():

    """
    >> 1 - Simplicity. Integration needs to be dead simple.
    2 - Resilient to network failures or crashes.
    3 - Near real time replication of data across Geolocation. Writes need to be in real time.
    4 - Data consistency across regions
    5 - Locality of reference, data should almost always be available from the closest region
    >> 6 - Flexible Schema
    >> 7 - Cache can expire 

    Considering the difficulty of the task and my lack of knowledge of geolocalisation cache,
    I decided to implement a timed cache that can contain a list object of any filled with any types,
    as long as the list has the pop and append methods.

    After the expiration time, the cache is invalid and needs to be recreated,
    so we delete all the cached items to allow the python3 garbage collector to free up memory space.


    Idea for geo localised cache :
    keep the mechanic implemented here, but also define geo location zones where there would be one server
    per zones. Reroute all cache demand per zone to their respective server.

    This algorithm would be possibly more efficient if
    writen in c++, and even more in C, and then even more in assembly

    The time im going to use is going to be a time object from the datetime modules.
    https://docs.python.org/3.4/library/datetime.html

    I will also use the time module to get the data for the creation of the datetimw object.
    https://docs.python.org/3.4/library/time.html#time.ctime

    The reason I do this is because the datetime object allows manipulation of it like any good object
    therefore easier manipulation and comparison of these objects.
    """

    def __init__(self,items,expiration_time,size):
        """
        items : list object with pop and append method
        expiration_time : is a datetime object of the time
        size: an integer representing the cache size
        """
        self._size = size
        if len(items) > size:
            self._items = []
        else:
            self._items = items

        # get the current time and makes a date time object
        curr_time= time.gmtime()
        self._creation_time = datetime.datetime(curr_time.tm_year,curr_time.tm_mon,curr_time.tm_mday,curr_time.tm_hour,curr_time.tm_min,curr_time.tm_sec)

        self._expiration_time = expiration_time

    def add(self,item):
        # if the cache is expired , empty and
        # then procceed to return false to indicate that the cached expired a
        if self.isExpired():
            self.emptyCache()
            return False
        # if the cache has no place, remove the first list item, which is the least recently used
        # then procceed to return true to indicate that the item was added
        elif len(self._items) == self._size:
            del self._items[0]
            self._items.append(item)
            return True
        else:
            self._items.append(item)
            return True


    def __getitem__(self,key):
        """
        Take the item wanted by the person using the cache and put it first.
        Doing this makes the first item in the list the one most recently used
        and on the flipside, the one least recently used is at the first spot (index 0)
        """
        gotten_item = self._items[key]
        item_asked=self._items.pop(key)
        self._items.append(item_asked)
        return gotten_item

    def __delitem__(self,key):
        del self._items[key]


    def isExpired(self):
        """
        if the function return true the cache is expired
        which means that the expiration date is highger than the creation time
        """
        return self._expiration_time > self._creation_time


    def emptyCache(self):
        """
        Deletes the items in the cache, to let the garbage collector do its magic.
        """
        self._items.clear()
