#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, url_for, redirect, render_template, jsonify, make_response, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import numpy as np
import re


# In[2]:


app = Flask(__name__)

# Secret key (security)
app.secret_key = 'performancedashboard'

app.config['MYSQL_USER'] = 'sql3420283'
app.config['MYSQL_PASSWORD'] = 'Blcmsczqtr'
app.config['MYSQL_HOST'] = 'sql3.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql3420283'

mysql = MySQL(app)


# In[3]:


@app.route('/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    error = None
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM example WHERE username = %s AND password = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('home'))
        
        else:
            # Account doesnt exist or username/password incorrect
            error = 'Incorrect username/password!'
        
    # Show the login form with message (if any)
    return render_template('login.html', error=error)


# In[4]:


@app.route('/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('index.html', username=session['username'])


# In[5]:


@app.route('/resetpassword', methods=['GET', 'POST'])
def password():
    msg = None
    
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'new password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        newpassword = request.form['new password']
        
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM example WHERE username = %s AND password = %s', (username, password))
        
        account = cursor.fetchone()
        
        # If account exists in accounts table in out database
        if account:
            cursor.execute('UPDATE example SET password = %s  WHERE username = %s', (newpassword, username))
            mysql.connection.commit()
            return redirect(url_for('login'))
        else:
            msg="Username/password is wrong"
    
    return render_template('changepass.html', msg=msg)


# In[6]:


@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    # Redirect to login page
    return redirect(url_for('login'))


# In[7]:


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home'))

    # show the form, it wasn't submitted
    return render_template('dashboard.html')


# In[8]:


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home'))

    # show the form, it wasn't submitted
    return render_template('predict.html')


# In[9]:


if __name__ == "__main__":
    app.run()


# In[ ]:




