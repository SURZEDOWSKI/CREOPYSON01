# %%
import creopyson

c = creopyson.Client()
c.connect()

c.creo_set_creo_version(7)

c.is_creo_running()
creopyson.file_open(c, file_="projekt1.prt", dirname="C:/Users/Public/Documents/API_CAD/projekt")

def changeDim():
    try:
        print(creopyson.dimension.list_(c))
        print("Podaj nazwę wymiaru:")
        name = input()
        name = str(name)
        print("Podaj nową wartość wymiaru:")
        val = input()
        val = int(val)
        if name:
            if(val>0):
                c.dimension_set(name, val)
            else:
                print("Wrong attribute value")
        else:
            print("Wrong dim name!")
    except:
        print("Someting went wrong!")
    else:
        print(name, val)

def changeParam():
    try:
        print(creopyson.parameter.list_(c))
        print("Podaj nazwę parametru:")
        name = input()
        name = str(name)
        print("Podaj nową wartość parametru:")
        val = input()
        val = str(val)
        if name:
            creopyson.parameter.set_(c, name, val)
        else:
            print("Wrong param name!")
    except:
        print("Someting went wrong!")
    else:
        print(name, val)

def changeDir():
    try:
        print(c.creo_pwd())
        print("Podaj ścieżkę:")
        newDir = input()
        newDir = str(newDir)
        new = c.creo_cd(newDir)
    except:
        print("Wrong directory path")
    else:
        print(new) 

def changeMat():
    try:
        print(c.file_get_cur_material())
        print("Podaj nazwę materiału:")
        name = input()
        name = str(name)
        c.file_set_cur_material(name)
    except:
        print("Wrong material")
    else:
        current = c.file_get_cur_material()
        print(current)

def loadMat(name, src):
    try:
        for i in range(len(name)):
            c.file_load_material_file(name[i], src)
    except:
        print("Something went wrong!")
    else:
        print(name)

def loadNewMat():
    try:
        print("Podaj nazwę materiału:")
        name = input()
        name = str(name)
        print("Podaj ścieżkę:")
        src = input()
        src = str(src)
        c.file_load_material_file(name, src)
    except:
        print("Something went wrong!")
    else:
        print(name)

def start():
    run = True
    print("Zmień:\n1. Wymiar\n2. Parametr\n3. Folder roboczy\n4. Materiał\nAby zakończyć naciśnij \"Q\"")
    while(run):
        print("Wybierz opcję:")
        act = input()
        if act == "1":
            changeDim()
        elif act == "2":
            changeParam()
        elif act == "3":
            changeDir()
        elif act == "4":
            changeMat()
        elif act == "Q":
            run = False
        else:
            print("Podano złą wartość!")
        creopyson.file.regenerate(c)


loadMat(["Gold", "Lead", "Silver", "Nickel", "Tin", "Titanium", "Zinc", "Brass_cast", "Bronze_cast", "Copper_cast"], r"C:\Program Files\PTC\Creo 7.0.1.0\Common Files\text\materials-library\Standard-Materials_Granta-Design\Non-ferrous_metals")

#changeDim()
#changeParam()
#changeDir()
#changeMat()
#loadNewMat()

start()

#asdasdasd

print("1234")