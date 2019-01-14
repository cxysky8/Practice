import xlwt
import xlrd

SEARCHKEY="EMS编号"
SEARCHNAME="岗位"

if __name__ == "__main__":
    new_sheet=xlrd.open_workbook(r"users_new.xls").sheet_by_index(0)
    old_sheet=xlrd.open_workbook(r"users_old.xls").sheet_by_index(0)
    new_sheet_rowtitle=new_sheet.row_values(0)
    cmpdict_key_index=new_sheet_rowtitle.index(SEARCHKEY)
    cmpdict_name_index=new_sheet_rowtitle.index(SEARCHNAME)
    cmpdict={}
    for i in range(1,new_sheet.nrows):
        cmpdict_key=new_sheet.cell(i,cmpdict_key_index).value
        cmpdict_name=new_sheet.cell(i,cmpdict_name_index).value
        cmpdict[cmpdict_key]=cmpdict_name
    old_sheet_coltitle=old_sheet.row_values(0)
    ems_index=old_sheet_coltitle.index(SEARCHKEY)
    position_index=old_sheet_coltitle.index(SEARCHNAME)
    result=[]
    for i in range(1,old_sheet.nrows):
        ems=old_sheet.cell(i,ems_index).value
        if cmpdict.get(ems)!=None:
            position_old=old_sheet.cell(i,position_index).value
            position_new=cmpdict[ems]
            if position_new!=position_old:
                temp=ems+","+position_new+","+position_old
                result.append(temp)
    for resultOutPut in result:
        print(resultOutPut)

    

