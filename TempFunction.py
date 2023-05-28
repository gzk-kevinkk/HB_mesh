def generate_geo(filename, geo_filename="hb_model.geo.in"):
    f = open(geo_filename, "r")
    out_str = ""
    out_str += f.readline()
    out_str += f.readline()
    temp_str = f.readline()
    temp_str = temp_str.replace("hb_model.step", filename)
    out_str += temp_str
    for temp_str2 in f:
        out_str += temp_str2.replace("hb_model.mesh", filename.replace(".step", ".mesh"))
    f.close()
    new_name = filename.replace(".step", ".geo")
    f = open(new_name, "w")
    f.write(out_str)
    f.close()


def generate_bcmap(filename, n, dir="../input/"):
    out_filename = filename.replace(".step","_bcmap.txt")
    out_filename = dir + out_filename
    print(out_filename)
    f = open(out_filename, "w")
    n_face = 16 + 3 * n
    n_face_end = 18 + 3 * n
    out_str = str(n_face_end) + "\n"
    f.write(out_str)
    for i in range(1,17):
        if i == 5 or i == 11:
            out_str = str(i) + " " + "INTERFACE\n"
            f.write(out_str)
            # print(out_str)
        else:
            out_str = str(i) + " " + "DIRICHLET\n"
            f.write(out_str)
            # print(out_str)
    for i in range(19, n_face_end+1):
        out_str = str(i) + " " + "INTERFACE\n"
        f.write(out_str)
    f.close()

def generate_rmark(filename, n, model_type = "hb", model_description = "None", dir="../input/"):
    out_filename = filename.replace(".step","_rmark.txt")
    out_filename = dir + out_filename
    f = open(out_filename, "w")
    n_vol = 3 + n
    out_str = ""
    if model_type == "hb":
        out_str = "material_num 4" + "\n"
        out_str += "1 Si (E nu alpha)\n"
        out_str += "162.0e3 0.28 3.05e-6\n"
        out_str += "\n"
        out_str += "2 SiO2 (E nu alpha)\n"
        out_str += "71.7e3 0.16 5.1e-7\n"
        out_str += "\n"
        out_str += "3 TiN (E nu alpha)\n"
        out_str += "500.0e3 0.25 9.35e-6\n"
        out_str += "\n"
        out_str += "4 Cu (E nu alpha)\n"
        out_str += "111.5e3 0.343 1.77e-5\n"
        out_str += "\n"
    elif model_type != None or model_description != None:
        print("Do not support this kind of model now")
        exit(1)
    else:
        print("No material information!!!")
        exit(1)
    f.write(out_str)
    out_str = "region_mark_num " + str(n_vol) +"\n"
    f.write(out_str)

    if model_type == "hb":
        for i in range(1,3):
            out_str = str(i) + " " + "1\n"
            f.write(out_str)
        i = 3
        out_str = str(i) + " " + "2\n"
        f.write(out_str)
        for i in range(4,n_vol+1):
            out_str = str(i) + " " + "4\n"
            f.write(out_str)
    f.close()