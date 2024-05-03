import PySimpleGUI as sg

def main():
    # Modifying parameters
    choices = sorted([elem for elem in range(1, 1001)])  # Example: Choices are integers from 1 to 1001
    input_width = 15
    num_items_to_show = 6

    layout = [
        [sg.CB('Ignore Case', k='-IGNORE CASE-')],
        [sg.Text('Input Value:')],
        [sg.Input(size=(input_width, 1), enable_events=True, key='-IN-')],
        [sg.pin(sg.Col([[sg.Listbox(values=[], size=(input_width, num_items_to_show), enable_events=True, key='-BOX-',
                                    select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, no_scrollbar=True)]],
                       key='-BOX-CONTAINER-', pad=(0, 0), visible=False))]
    ]

    window = sg.Window('AutoComplete', layout, return_keyboard_events=True, finalize=True, font=('Helvetica', 16))

    list_element: sg.Listbox = window.Element('-BOX-')
    prediction_list, input_text, sel_item = [], "", 0

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event.startswith('Escape'):
            window['-IN-'].update('')
            window['-BOX-CONTAINER-'].update(visible=False)
        elif event.startswith('Down') and len(prediction_list):
            sel_item = (sel_item + 1) % len(prediction_list)
            list_element.update(set_to_index=sel_item, scroll_to_index=sel_item)
        elif event.startswith('Up') and len(prediction_list):
            sel_item = (sel_item + (len(prediction_list) - 1)) % len(prediction_list)
            list_element.update(set_to_index=sel_item, scroll_to_index=sel_item)
        elif event == '\r':
            if len(values['-BOX-']) > 0:
                window['-IN-'].update(value=values['-BOX-'])
                window['-BOX-CONTAINER-'].update(visible=False)
        elif event == '-IN-':
            text = values['-IN-'] if not values['-IGNORE CASE-'] else values['-IN-'].lower()
            if text == input_text:
                continue
            else:
                input_text = text
            prediction_list = []
            if text:
                if values['-IGNORE CASE-']:
                    prediction_list = [str(item) for item in choices if str(item).lower().startswith(text)]
                else:
                    prediction_list = [str(item) for item in choices if str(item).startswith(text)]

            list_element.update(values=prediction_list)
            sel_item = 0
            list_element.update(set_to_index=sel_item)

            if len(prediction_list) > 0:
                window['-BOX-CONTAINER-'].update(visible=True)
            else:
                window['-BOX-CONTAINER-'].update(visible=False)
        elif event == '-BOX-':
            window['-IN-'].update(value=values['-BOX-'])
            window['-BOX-CONTAINER-'].update(visible=False)

    window.close()


if __name__ == '__main__':
    main()