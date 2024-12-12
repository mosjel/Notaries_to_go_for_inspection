import tkinter as tk
from tkinter import font
import os
import pandas as pd
from openpyxl import load_workbook
import numpy as np
import jdatetime
import openpyxl.utils.cell

def display_right_aligned_text(root, process_label):
    # Farsi text content
    s = [
        "--------------------تندر افزار نرم--------------------",
        "(بازرسی جهت رسمی اسناد دفاتر نوبت تعیین)",
        "1403 بهار - 1.2 نسخه",
        "نسخه 1.1",
        "-------------------------",
        "جلوه مصطفی",
        "Email: mostafaajelveh@gmail.com"
    ]

    # Create a Text widget for multiline display
    text_widget = tk.Text(root, wrap=tk.WORD, bg='black', fg='white', font=('Arial', 14), relief='flat', spacing1=5, spacing2=5, spacing3=5)
    text_widget.pack(expand=True, fill='both')

    # Set tags for right-to-left (RTL) alignment
    text_widget.tag_configure('right', justify='right')
    text_widget.tag_configure('center', justify='center')
    
    # Insert lines with center alignment
    for num, line in enumerate(s):
        if num < 5:
            text_widget.insert(tk.END, line.center(50, '-') + '\n', ('green_bold', 'center'))
        else:
            text_widget.insert(tk.END, line.center(50, '-') + '\n', ('white_bold', 'center'))

    text_widget.insert(tk.END, '\n' * 4)

    # Insert lines with right alignment
    for _ in range(7):
        text_widget.insert(tk.END, '*' * 50 + '\n', 'red_bold')

    text_widget.insert(tk.END, '\n\n' + process_label.rjust(50) + '\n', 'blue_bold')

    # Configure tags for styling
    text_widget.tag_config('green_bold', foreground='#00FF00', font=('Arial', 14, 'bold'))
    text_widget.tag_config('white_bold', foreground='#FFFFFF', font=('Arial', 14, 'bold'))
    text_widget.tag_config('red_bold', foreground='#FF0000', font=('Arial', 14, 'bold'))
    text_widget.tag_config('blue_bold', foreground='#0000FF', font=('Arial', 14, 'bold'))

    # Disable editing in the Text widget
    text_widget.config(state='disabled')

    root.after(5000, lambda: root.destroy())  # Close window after 5 seconds

def persian_to_georgian(persian_date):
    try:
        if persian_date:
            date_list = [int(i) for i in persian_date.split("/")]
            gregorian_date = jdatetime.date(date_list[0], date_list[1], date_list[2]).togregorian()
            return gregorian_date
    except Exception as e:
        return "Error"

def forward_fill_merged(df, merged_ranges):
    for merged_range in merged_ranges:
        start_cell, end_cell = merged_range.split(':')

        # Convert cell addresses to indices
        start_row, start_col = openpyxl.utils.cell.coordinate_to_tuple(start_cell)
        end_row, end_col = openpyxl.utils.cell.coordinate_to_tuple(end_cell)

        # Adjust for zero-based indexing in pandas
        start_row -= 2
        end_row -= 1
        start_col -= 1

        # Select the range in the DataFrame
        sub_df = df.iloc[start_row:end_row, start_col:end_col]
        
        # Apply forward fill to the range
        sub_df = sub_df.ffill(axis=0)

        # Put the filled values back into the original DataFrame
        df.iloc[start_row:end_row, start_col:end_col] = sub_df

def main():
    try:
        dir_name = os.path.dirname(os.path.abspath(__file__))
        os.system('cls' if os.name == 'nt' else 'clear')
        error_label = ": شد مواجه خطا با فایل ایجاد"
        process_label = "......[notary_visited_total.xlsx] فایل اطلاعات پردازش حال در"
        success_label = ".شد ایجاد موفقیت با [notaries_togo.xlsx]  فایل"
        success_label_1 = u'\u2713' + " " + "باشید موفق"

        root = tk.Tk()
        root.title("Processing")
        root.geometry("700x400")

        display_right_aligned_text(root, process_label)

        root.mainloop()

        file_path = os.path.join(dir_name, "total.xlsx")
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook['Sheet1']

        merged_cells_ranges = [merged_range.coord for merged_range in sheet.merged_cells.ranges]

        column_dtype = {6: str, 4: str}
        df = pd.read_excel(file_path, engine='openpyxl', usecols=list(range(0, 7)), sheet_name="Sheet1", dtype=column_dtype)
        df[df.columns[6]] = df[df.columns[6]].fillna("")
        last_valid_index = df.iloc[:, 6].last_valid_index()
        df = df.iloc[:last_valid_index + 1, :]

        forward_fill_merged(df, merged_cells_ranges)

        grouped = df.groupby(df.columns[[0, 1, 2, 3, 4, 5]].tolist(), dropna=False).apply(lambda x: x.index.min() + 2).reset_index()
        df_merged = df.groupby(df.columns[[0, 1, 2, 3, 4, 5]].tolist(), dropna=False)[df.columns[6]].apply(lambda x: '*'.join(x)).reset_index()
        df_merged["Excel_Index"] = grouped[grouped.columns[6]]

        visited_notaries = np.array(df_merged[df_merged.columns[4]])
        df_notary = pd.read_excel(os.path.join(dir_name, "notary_list.xlsx"), dtype={0: str})
        notary_list = np.array(df_notary["لیست دفترخانه های تهران"])
        notary_list_not_visited_index = np.invert(np.isin(notary_list, visited_notaries))
        notary_mistakes_index = np.invert(np.isin(visited_notaries, notary_list))

        df_merged[df_merged.columns[2]] = df_merged[df_merged.columns[2]].fillna("")
        df_merged["georgian"] = df_merged[df_merged.columns[2]].apply(persian_to_georgian)

        df_error = df_merged[df_merged[df_merged.columns[8]] == "Error"]
        df_na = df_merged[df_merged[df_merged.columns[8]].isnull()].copy()
        df_na[df_na.columns[2]] = "Mistake Risk"
        df_na_violated = df_na[df_na[df_na.columns[5]] != "عدم تخلف"]
        df_na_not_violated = df_na[df_na[df_na.columns[5]] == "عدم تخلف"]

        df_merged[df_merged.columns[8]] = pd.to_datetime(df_merged[df_merged.columns[8]], errors="coerce").dt.date
        df_mistake_risk = df_merged[notary_mistakes_index].copy()
        df_mistake_risk["شماره دفترخانه اشتباه"] = "Mistake"
        df_merged.dropna(subset=[df_merged.columns[8]], inplace=True)

        df_dates = df_merged[df_merged.groupby(df_merged.columns[4], dropna=False)[df_merged.columns[8]].transform("max") == df_merged[df_merged.columns[8]]]
        df_sorted_dates_violated = df_dates[df_dates[df_dates.columns[5]] != "عدم تخلف"].sort_values(df_dates.columns[8], ascending=True)
        df_sorted_dates_not_violated = df_dates[df_dates[df_dates.columns[5]] == "عدم تخلف"].sort_values(df_dates.columns[8], ascending=True)

        notary_list_not_visited = notary_list[notary_list_not_visited_index]
        empty_df = pd.DataFrame('', index=range(len(notary_list_not_visited)), columns=df_mistake_risk.columns)
        empty_df[empty_df.columns[4]] = notary_list_not_visited

        df_mistake_and_not_visited = pd.concat([df_mistake_risk, empty_df])
        df_final = pd.concat([df_mistake_and_not_visited, df_error, df_na_violated, df_sorted_dates_violated, df_sorted_dates_not_violated], axis=0)
        df_final.fillna("")

        df_org = df_final.reset_index(drop=True)
        df_org.insert(0, "شماره اصلی", value=list(range(1, df_org.shape[0] + 1)))
        df_org.rename

if __name__ == "__main__":
    main()
