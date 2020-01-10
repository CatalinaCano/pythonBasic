

def decotator_validate_sms(func):
    def validate_data (phone, message):
        if phone.isdigit() and len(message)>0:
            return func(phone,message)
        else:
            print('Oohh sorry, the data it\'s Ivalid ')
    return validate_data

@decotator_validate_sms
def send_sms(phone, message):
    print('Sending SMS , to {} with the message {}'.format(phone,message))
    
  
def capture_options():
     phone = str(input('Enter phone number: \n'))
     message = str(input('Enter the message \n'))
     send_sms(phone,message)
  
def run():
    while True:        
        print('============== SENDING SMS ===============')
        option = str(input('Please choose one option \n (S)ending Messages \n (E)xit \n \t')).upper()
        if option=='S':
           capture_options()
        else:
            break
            
            
        
if __name__ == '__main__':
    try:
        run()
    except :
        print('Ooooh sorry one mistake happened!! ')
        run()

    