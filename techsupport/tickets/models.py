from datetime import datetime
import json
from unittest import result
from urllib import request
from flask import Flask, jsonify, request, session, render_template, redirect
from passlib.hash import pbkdf2_sha256
from .. import ticket_db
from bson import ObjectId

class Ticket():
    def fetch_ticket(id):
        print('------mark----')

        result = ticket_db.find_one({'_id': id})

        print('***********')
        print(result)
        print('***********')

        ticket = {
        "_id": str(result['_id']),
        "ticket_status": result['ticket_status'],
        "assigned_to": result['assigned_to'],
        "name": result['name'],
        "email": result['email'],
        "title": result['title'],
        "desc": result['desc'],
        }

        print('***********')
        print(ticket)
        print('***********')

        return render_template('edit_ticket.html', ticket=ticket, year=datetime.now().year)

    def fetch_tickets():
        
        for x in ticket_db.find():
            print(x)
            x['_id'] = str(x['_id'])
        return ticket_db.find()        

    def create_ticket(self):

        #create ticket object
        ticket = {
            #"_id": uuid.uuid4().hex,
            "ticket_status": "Open",
            "assigned_to": "Unassigned",
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "title": request.form.get('title'),
            "desc": request.form.get('desc'),
            }


        #database
        result = ticket_db.insert_one(ticket)
        if result.inserted_id:
            return jsonify(str(result.inserted_id)), 200
        
        return jsonify({ "error": "Process failed" }), 400

    def edit_ticket(self):

        ticket = {
            "_id": request.form.get('id'),
            "ticket_status": request.form.get('ticket_status'),
            "assigned_to": request.form.get('assigned_to'),
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "title": request.form.get('title'),
            "desc": request.form.get('desc'),
            }
        #print(ticket['_id'])
        x = ticket_db.find_one({'_id': ticket['_id']})
        print('------------')
        print(x)
        print('------------')
        #return jsonify(x), 418

        result = ticket_db.update_one({'_id': ObjectId(ticket['_id'])}, {
            '$set':
                {
                    'ticket_status':ticket['ticket_status'],
                    'assigned_to':ticket['assigned_to'],
                    'name':ticket['name'],
                    'email':ticket['email'],
                    'title':ticket['title'],
                    'desc':ticket['desc']
                    }
            }
                                )
        if result.modified_count == 1:

            print('------------')
            print(ticket)
            print('------------')
            return jsonify(ticket), 200

        return jsonify({ "error": "Process failed" }), 400

