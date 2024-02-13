import sqlite3
import os
from cs50 import SQL
import urllib.parse
from flask import redirect, render_template, request, session
from functools import wraps
from random import randint

db = SQL("sqlite:///data/ia.db")

def login_required(f):
    " Decorate routes to require login. https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/"
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def count_digits(n):
    count = 0
    while n!=0:
        n = int(n)
        n //= 10
        count +=1
    return count


class user:
    def __init__(self, user_id, user_name, description, password):
        self.user_id = user_id
        self.user_name = user_name
        self.description = description
        self.password = password   
    def save(self):
        sql = db.execute("INSERT INTO users (user_id, user_name, description, password) VALUES (?, ?, ?, ?);", self.user_id, self.user_name, self.description, self.password)
    def remove(self):
        sql = db.execute("DELETE FROM users WHERE user_id = ?;", self.user_id) 
    
class employee(user):
    def __init__(self, user_id, user_name, description, password):
        self.user_id = user_id
        self.user_name = user_name
        self.description = description
        self.password = password

class customer(user):
    def __init__(self, user_id, user_name, description, password):
        self.user_id = user_id
        self.user_name = user_name
        self.description = description
        self.password = password    

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
 
class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
 
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]
 
    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0
 
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
 
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
 
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value
 
def generate_unique_order_id(orderids):
    order_id = randint(1000, 9999)
    if order_id in orderids:
        return generate_unique_order_id(orderids)  # Recursive call
    return order_id




    