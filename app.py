import json
import random
from flask import Flask, Response
from User import User
from Card import CARDS

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

first_user = User(name="test1", cards=[CARDS.get("Винный завод"), CARDS.get("Виноградник")])
second_user = User(name="test2", cards=[CARDS.get("Траулер")])
current_user_index = 0


def get_key(ID):
    for key, value in CARDS.items():
        if ID == value.ID:
            return key
    return "key doesn't exist"

second_user.cards.append(CARDS.get(get_key('B2')))
# print(second_user.cards)

users = [first_user, second_user]


@app.route('/')
def root():
    # result_str = "Roll: %d\nUser: %s\n" % (roll, users[pv].name)
    global current_user_index
    pv = current_user_index
    current_user_index += 1
    if current_user_index >= len(users):
        current_user_index = 0

    # roll = random.randint(1, 6)
    roll = random.randint(2, 12)

    for index, user in enumerate(users):
        user.do_move(roll, current_user_index == index)

    result_str = "%d,\n" % roll
    for index, user in enumerate(users):
        result_str += json.dumps({
            "name": user.name,
            "money": user.money,
            "turn": current_user_index == index
        }, indent=4) + ',\n'


    return Response(result_str, mimetype="application/json")


@app.route('/<int:number>')
def run_more_that_once(number):
    for i in range(number):
        root()
    result_str = ""
    for user in users:
        result_str += json.dumps({
            "name": user.name,
            "money": user.money,
        }, indent=4) + ',\n'
    return Response(result_str, mimetype="application/json")

@app.route('/<cardID>')
def addcard(cardID):
    global current_user_index
    users[current_user_index].cards.append(CARDS.get(get_key(cardID)))

