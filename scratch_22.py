import tkinter
from tkinter import *
from tkinter import ttk
from poki_api import get_poke_info

def main():

    root = Tk()



    root.title('Pokemon Stats')

    frm_input = ttk.Frame(root)
    frm_input.grid(row=0, column=1)

    frm_stats = ttk.LabelFrame(root, text='Stats')
    frm_stats.grid(row=2, column=1, columnspan=2)

    frm_info = ttk.LabelFrame(root, text='Info')
    frm_info.grid(row=1, column=1, padx=(0,15), pady=10)

    lbl_name = ttk.Label(frm_input, text='Name '':')
    lbl_name.grid(row=0, column=0)

    ent_name = ttk.Entry(frm_input)
    ent_name.grid(row=0, column=1)

    def btn_get_info():
        name = ent_name.get()
        poke_dict = get_poke_info(name)
        if poke_dict:
            lbl_height_val['text'] = str(poke_dict['height']) + ' dm'
            lbl_weight_val['text'] = str(poke_dict['weight']) + ' hg'

            types_list = [t['type']['name'] for t in poke_dict['types']]
            lbl_type_val['text'] = ', '.join(types_list)
            prg_hp['value'] = poke_dict['stats'][0]['base_stat']
            prg_attk['value'] = poke_dict['stats'][1]['base_stat']
            prg_def['value'] = poke_dict['stats'][2]['base_stat']
            prg_sa['value'] = poke_dict['stats'][3]['base_stat']
            prg_sd['value'] = poke_dict['stats'][4]['base_stat']
            prg_speed['value'] = poke_dict['stats'][5]['base_stat']

    btn_getinfo = ttk.Button(frm_input, text='Get Info', command=btn_get_info)
    btn_getinfo.grid(row=0, column=2, padx=15, pady=10)

    lbl_hp = ttk.Label(frm_stats, text='HP:')
    lbl_hp.grid(row=0, column=0, padx=10, pady=10, sticky=E)
    prg_hp = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_hp.grid(row=0, column=1)

    lbl_attk = ttk.Label(frm_stats, text='Attack:')
    lbl_attk.grid(row=1, column=0, padx=10, pady=10, sticky=E)
    prg_attk = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_attk.grid(row=1, column=1)

    lbl_def = ttk.Label(frm_stats, text='Defence:')
    lbl_def.grid(row=2, column=0, padx=10, pady=10, sticky=E)
    prg_def = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_def.grid(row=2, column=1)

    lbl_sa = ttk.Label(frm_stats, text='Special Attacks:')
    lbl_sa.grid(row=3, column=0, padx=10, pady=10, sticky=E)
    prg_sa = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_sa.grid(row=3, column=1)

    lbl_sd = ttk.Label(frm_stats, text='Special Defense:')
    lbl_sd.grid(row=4, column=0, padx=10, pady=10, sticky=E)
    prg_sd = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_sd.grid(row=4, column=1)

    lbl_speed = ttk.Label(frm_stats, text='Speed:')
    lbl_speed.grid(row=5, column=0, padx=10, pady=10, sticky=E)
    prg_speed = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_speed.grid(row=5, column=1)


    lbl_height = ttk.Label(frm_info, text='Height:')
    lbl_height.grid(row=2, column=3, padx=15, pady=15)
    lbl_height_val= ttk.Label(frm_info, text='N/A')
    lbl_height_val.grid(row=2, column=4, padx=10, pady=15)

    lbl_weight = ttk.Label(frm_info, text='Weight:')
    lbl_weight.grid(row=1, column=3)
    lbl_weight_val= ttk.Label(frm_info, text='N/A')
    lbl_weight_val.grid(row=1, column=4, padx=10, pady=15)

    lbl_type= ttk.Label(frm_info, text='Type:')
    lbl_type.grid(row=3, column=3, padx=10, pady=15)
    lbl_type_val = ttk.Label(frm_info, text='N/A')
    lbl_type_val.grid(row=3, column=4, padx=10, pady=15)














    

    root.mainloop()


main()