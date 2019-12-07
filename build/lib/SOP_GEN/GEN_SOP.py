# @Author: genli
# @Date:   2019-11-17T15:59:26-05:00
# @Last modified by:   genli
# @Last modified time: 2019-11-17T20:13:21-05:00



import pandas as pd
import os
import glob
from docx import Document

class GEN_SOP(object):

    """
    Distributed model class

    Parameters
    ----------
    school_list : string
        The excel file path where A list of schools and programs is saved.
    SOP_temp_file : string
        The docx file path of your SOP template.
    School : string
        The column name where the school name is saved.
    Program : string
        The column name where the program info is saved.
    output_path : string
        Output path where you want to save your output files.

    Examples
    --------

    Notes
    -----
    
    """

    def __init__(self,school_list,SOP_temp_file,School_var='School',Program_var='Program',output_path=os.getcwd()):
        self.school_list = school_list
        self.SOP_temp_file = SOP_temp_file
        self.School = School_var
        self.Program = Program_var
        self.output_path = output_path


    def gen_sop(self):
        os.chdir(self.output_path)

        # ==================
        #   Import school list
        # ==================
        df_school = pd.read_excel(self.school_list)
        df_school[self.School] = df_school[self.School].str.replace('\s+',' ').str.strip()

        # ==================
        #   Create Folder
        # ==================
        df_school['school_folder'] = df_school[self.School].str.replace('\s|\,|\.', '_')
        df_school['school_folder'] = df_school['school_folder'].str.replace('\_+','_')

        for p in df_school.Program.unique():
            if os.path.isdir('./' + p) == 0:
                os.mkdir(p)

        # ==================
        #   Create Statement File
        # ==================
        filename = self.SOP_temp_file

        for n in range(df_school.shape[0]):
            doc = Document(filename)
            for p in doc.paragraphs:
                if '[SCHOOL_NAME]' in p.text:
                    inline = p.runs
                    for i in range(len(inline)):
                        if '[SCHOOL_NAME]' in inline[i].text:
                            text = inline[i].text.replace('[SCHOOL_NAME]', df_school.School[n])
                            inline[i].text = text


                if '[PROGRAM_NAME]' in p.text:
                    inline = p.runs
                    for i in range(len(inline)):
                        if '[PROGRAM_NAME]' in inline[i].text:
                            text = inline[i].text.replace('[PROGRAM_NAME]', df_school.Program[n])
                            inline[i].text = text

            doc.save(df_school.Program[n] + '/' + df_school.school_folder[n] + '.docx')
            print("The SOP for " + df_school.Program[n] + " program in " + df_school.School[n] + " is ready.")


if __name__ == "__main__":
    current_path = os.getcwd()
    GEN_SOP(current_path + '/school_list.xlsx',current_path + '/SOP_template.docx').gen_sop()
