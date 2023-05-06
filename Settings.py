import os
from fileinput import filename


class Settings():

    def getIni(self):
        if os.path.exists(self.pathIni):

                init = open(self.pathIni, 'r').readlines()
                i = 0
                ini = {}
                while i < len(init) - 1:
                    if ':' in init[i]:
                        j = i+1
                        lines = {}
                        while (not ':' in init[j]) and j < len(init) -1:
                            if '=' in init[j]:
                                line = init[j].replace('\n', '').split("=")
                                lines.update({line[0]: line[1]})
                            j += 1
                        ini.update({init[i].replace(':\n', ''): lines})
                        i = j-1
                    i += 1



                #CHECK



                for path in ini["PATHS"].keys():
                    if not (os.path.exists(ini["PATHS"][path])):
                        raise Exception(f"path {ini['PATHS'][path]} for {path} not found or doesn't exist")



                need = ['RPDs', 'Plans', 'Text','Deploy','sh']
                for name in need:
                    if not (name in ini['PATHS'].keys()):
                        raise Exception(f"{name} path reqired")
                return ini

        else:
            raise Exception("settings.ini not found")



    def __init__(self) -> None:
        self.pathIni = "settings.ini"
        self.ini = self.getIni()
        self.Plans = [self.ini["PATHS"]["Plans"]+'/'+file for file in os.listdir(self.ini["PATHS"]["Plans"])]
        self.RPDs = [self.ini["PATHS"]["RPDs"]+'/'+file for file in os.listdir(self.ini["PATHS"]["RPDs"])]
        self.Text =[self.ini["PATHS"]["Text"]+'/'+file for file in os.listdir(self.ini["PATHS"]["Text"])]
        
