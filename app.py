#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from flask import Flask, request, url_for, redirect, render_template, jsonify, make_response, Blueprint


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route('/')
def home():
    return render_template('index.html')


# In[4]:


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home'))

    # show the form, it wasn't submitted
    return render_template('dashboard.html')


# In[5]:


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home'))

    # show the form, it wasn't submitted
    return render_template('predict.html')


# In[ ]:


if __name__ == "__main__":
    app.run()

