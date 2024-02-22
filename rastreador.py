import math

class rastreador:
    # inicializamos variables
    def __init__(self):

        self.centro_puntos = {} #   se almacena las posciones centrales de los obejetos

        self.id_contador =1 #contador de vehiculos detectados
    
    def rastreo(self,objetos):

        objetos_id = [] # lista donde se va almacenar obejtos identificados
        #obetnemos el puntro central del nuevo objeto
        for rect in objetos:
            x, y, w, h = rect 
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

             #miramos si el objeto ya fue detectado
            objeto_det = False
            for id, pt in self.centro_puntos.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                if dist < 25 :
                    self.centro_puntos[id] =(cx, cy)
                    print(self.centro_puntos)
                    objetos_id.append([x, y, w, h, id])
                    objeto_det = True
                    break 

            #si se detecta un nuevo objeto se la asigna un ID 
            if objeto_det is False:
                self.centro_puntos[self.id_contador] = (cx,cy) #almacenamos cordenadas x , y
                objetos_id.append([x, y, w, h, self.id_contador]) #  Agregamos a la lista el objeto
                self.id_contador = self.id_contador + 1
        #Se limpia la lista de vehiculos que ya no se detectan
        new_center ={}
        for obj_bb_id in objetos_id:
            _, _, _, _, objetos_id = obj_bb_id
            center = self.centro_puntos[objetos_id]
            new_center[objetos_id]= center
        
        self.centro_puntos = new_center.copy()

        return objetos_id

        

    

        