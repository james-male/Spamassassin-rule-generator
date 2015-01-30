import datetime

now = datetime.datetime.now()
currentDate = (now.strftime("%d%m%y"))

rule_number = 0
print()

def generate_rawbody():
    global rule_number
    rule_number += 1
    print('rawbody    LOCAL_SPAM' + currentDate + '_' + str(rule_number) + ' //i')
    print('describe   LOCAL_SPAM' + currentDate + '_' + str(rule_number) + ' Spammy phrase "" - in the body of message')
    print('score      LOCAL_SPAM' + currentDate + '_' + str(rule_number) + ' 1')
    print()


def generate_header():
    global rule_number
    rule_number += 1
    print('header     LOCAL_SPAM' + currentDate + '_' + str(rule_number) + ' =~ //i')
    print('describe   LOCAL_SPAM' + currentDate + '_' + str(rule_number) + ' Spam header in subject line ""')
    print('score      LOCAL_SPAM' + currentDate + '_' + str(rule_number) + ' 1')
    print()


def generate_uri():
    global rule_number
    rule_number += 1
    print('uri        LOCAL_SPAM' + currentDate + '_' + str(rule_number) + ' //i')
    print('describe   LOCAL_SPAM' + currentDate + '_' + str(rule_number) + ' Contains a suspicious link ""')
    print('score      LOCAL_SPAM' + currentDate + '_' + str(rule_number) + ' 1')
    print()


def generate_mimeheader():
    global rule_number
    rule_number += 1
    print('mimeheader LOCAL_SPAM' + currentDate + '_' + str(rule_number) + ' =~ //i')
    print('describe   LOCAL_SPAM' + currentDate + '_' + str(rule_number) + ' Email contains a suspicious attachment ""')
    print('score      LOCAL_SPAM' + currentDate + '_' + str(rule_number) + ' 1')
    print()

specify_ammount = input('How many rules would you like? ')
print()

print('please select the type of rule you want using the below prompts')
print('type \'raw\' for raw body rules')
print('press \'header\' for header rules')
print('press \'uri\' for uri rules')
print('press \'mime\' mime header rules')
print()
specify_type = input(' > ')


if specify_type == 'raw':
    for _ in range(int(specify_ammount)):
        generate_rawbody()


if specify_type == 'header':
    for _ in range(int(specify_ammount)):
        generate_header()


if specify_type == 'uri':
    for _ in range(int(specify_ammount)):
        generate_uri()


if specify_type == 'mime':
    for _ in range(int(specify_ammount)):
        generate_mimeheader()