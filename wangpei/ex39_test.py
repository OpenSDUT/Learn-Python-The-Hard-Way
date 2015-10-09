#!/usr/bin/env python
# coding=utf-8
#aMap 一个list，里面包括多个bucket
#bucket，一个list，里面包括多个slot
#slot，一个tuple，存的就是里面的key和value值 
def new(num_buckets=256):
    '''Initializes a Map with the given number of buckets'''
    aMap = []
    for i in range(0,num_buckets):
        aMap.append([])
    return aMap
def hash_key(aMap,key):
    '''Given a key this will create a numebr and then convert it to an index 
    for aMap's buckets.
    '''
    return hash(key)%len(aMap)#hash后对amap长度取余，怕重复冲突因此amap里都是list
def get_bucket(aMap,key):#get_bucket主要是通过key值来找到map存储在哪个bucket里
    '''Given a key,find the bucket where it would go.'''
    bucket_id = hash_key(aMap,key)
    return aMap[bucket_id]
def get_slot(aMap,key,default=None):#一个slot存一个map，通过aMap和key找到对应的slot
    '''returns the index,key,and value of a slot found in a bucket.returns-1,key,and 
    default(None if Not set)when not found'''
    bucket = get_bucket(aMap,key)
    for i,kv in enumerate(bucket):
        k,v = kv #kv就是一个slot，是一个tuple
        if key==k:
            return i,k,v
    return -1,key,default
def get(aMap,key,default=None):
    '''Gets the value in a bucket for the given key.or the default'''
    i,k,v = get_slot(aMap,key,default=default)
    return v
def set(aMap,key,value):
    '''sets the key to the value,replacing any existing value'''
    bucket = get_bucket(aMap,key)
    i,k,v = get_slot(aMap,key)
    
    if i>=0:
        #the key exists,replace it
        bucket[i]=(key,value)
    else:
        #the key does not,append to create it
        bucket.append((key,value))
def delete(aMap,key):
    '''deletes the given key from the map'''
    bucket = get_bucket(aMap,key)
    for i in xrange(len(bucket)):
        k,v = bucket[i]
        if key==k:
            del bucket[i]
            break
def list(aMap):
    '''prins out what's in the map'''
    for bucket in aMap:
        if bucket:
            for k,v in bucket:
                print(k,v)
