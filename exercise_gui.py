import PySimpleGUI as sg
from neededfunction import feet_and_inches_to_meters
import time


sg.theme('Black')

label_text = sg.Text('Enter feet:')
input_text = sg.InputText(tooltip='Type in feet', key='feet')

label_text2 = sg.Text('Enter inches:')
input_text2 = sg.InputText(tooltip='Type in inches', key='inches')

exit_button = sg.Button('Exit', key='Exit')

convert_button = sg.Button('Convert')
output_label = sg.Text(key='output')

window = sg.Window('Convertor', 
                   font = ('Helvetica', 20), 
                   layout=[[label_text, input_text], 
                           [label_text2, input_text2], 
                           [convert_button, output_label], 
                           [exit_button]])

while True:
    try:
        event, values = window.read()
        feet = float(values['feet'])
        inches = float(values['inches'])
    
        result = feet_and_inches_to_meters(feet, inches)
        window['output'].update(value=f'{result}m', text_color='white')
        window['clock'].update(time.strftime('%d:%m:%Y'))
    except ValueError:
        sg.popup('Please provide the numbers', font=('Helvetica', 10))


window.close()