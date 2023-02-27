import math
import random
import numpy as np


class AGTSP:

    Gen = []

    def __init__(self, tamPOB, iterMAX, pMUTAR, pCRUZAR, pSEL, Matriz, PosInicial):
        self.tamPOB = tamPOB
        self.iterMAX = iterMAX
        self.pMUTAR = pMUTAR
        self.pCRUZAR = pCRUZAR
        self.pSEL = pSEL
        self.Matriz = Matriz
        self.nodos = len(Matriz)
        self.PosInicial = PosInicial
        self.NumHijos = self.pCRUZAR * self.tamPOB  #Debe ser par
        self.NumMutaciones = self.pMUTAR * self.tamPOB

    def GetPosRep(self, IncluidoMin, ExcluidoMAX, Cantidad):
        Pos = np.random.randint(IncluidoMin, ExcluidoMAX, Cantidad).ravel().tolist()
        return Pos

    def GetPosNoRep(self,IncluidoMin, ExcluidoMAX, Cantidad):
        Pos = []
        BaseNum = []
        for i in range(int(IncluidoMin),int(ExcluidoMAX)):
            BaseNum.append(i)

        for j in range(int(Cantidad)):
            Index = random.randint(0, len(BaseNum) - 1)
            Pos.append(BaseNum[Index])
            BaseNum.pop(Index)
        return Pos

    def PosMejorMaximos(self,a,k):
        nMax = []
        Mejores = []
        n = 0
        for i in a:
            nMax.append(i)
        while n < k:
            m = a.index(max(nMax))
            Mejores.append(m)
            nMax.remove(max(nMax))
            n = n + 1
        
        return Mejores

    def PosMejorMinimos(self,a,k):
        nMin = []
        Mejores = []
        n = 0
        for i in a:
            nMin.append(i)
        while n < k:
            m = a.index(min(nMin))
            Mejores.append(m)
            nMin.remove(min(nMin))
            n = n + 1
        return Mejores

    def ExtraerCrom(self,PadreOmadre):
        Hij = []
        a = random.randint(1, self.nodos)
        for i in range(a):
            Hij.append(PadreOmadre[i])
        return Hij

    def EsFactible(self,Sol):


        if Sol[0] != self.PosInicial:
            return False

        else:
            return True

    def Beneficio(self,Sol):
        Isol = Sol[0]
        FSol = Sol[self.nodos-1]
        BeneficioSol = self.Matriz[Isol,FSol]

        for i in range(self.nodos - 1):
            ini = Sol[i]
            fin = Sol[i + 1]
            D = self.Matriz[ini, fin]
            BeneficioSol = BeneficioSol + D
        return BeneficioSol

    def Perturbar(self,Sol):
        random.shuffle(Sol)
        return Sol

    def Mutar(Self,Sol):


        NuevaSol = Sol.copy()

        while True:
            B = AGTSP.Perturbar(Self,NuevaSol)

            if AGTSP.EsFactible(Self,B) == True:

                NuevaSol = B
                break

        return NuevaSol

    def Cruzar(Self, Padre, Madre):

        Cromosomas1 = AGTSP.ExtraerCrom(Self,Padre)
        Cromosomas2 = AGTSP.ExtraerCrom(Self,Madre)
        PosH = len(Cromosomas1)
        PosM = len(Cromosomas2)
        restantesH = Self.nodos - PosH
        restantesM = Self.nodos - PosM

        while restantesH > 0:
            for j in range(Self.nodos):
                if Madre[j] not in Cromosomas1:
                    Cromosomas1.append(Madre[j])
                    restantesH = restantesH - 1

        while restantesM > 0:
            for k in range(Self.nodos):
                if Padre[k] not in Cromosomas2:
                    Cromosomas2.append(Padre[k])
                    restantesM = restantesM - 1

        Hijo = Cromosomas1
        Hija = Cromosomas2

        HijoMutado = AGTSP.Mutar(Self,Hijo)
        HijaMutada = AGTSP.Mutar(Self,Hija)



        return HijoMutado,HijaMutada

    def GenerarSol(Self):
        combinacion = []
        for i in range(Self.nodos):
            combinacion.append(i)
        random.shuffle(combinacion)
        return combinacion

    def ConstruirPobInicial(Self):
        for i in range(Self.tamPOB):
            Self.Gen.append(AGTSP.GenerarSol(Self))

    def CruzarGen(Self):
        PosPadres = AGTSP.GetPosNoRep(Self,0,Self.tamPOB,Self.NumHijos)

        for i in range(0,int( Self.NumHijos), 2):

            NuevosHijos = AGTSP.Cruzar(Self,Self.Gen[PosPadres[i]], Self.Gen[PosPadres[i + 1]])
            for v in NuevosHijos:
                Self.Gen.append(v)

    def MutarGen(Self):
        Pos= AGTSP.GetPosNoRep(Self,0,Self.tamPOB,Self.NumMutaciones)

        for i in range(int(Self.NumMutaciones)):
            SolMutada = AGTSP.Mutar(Self, Self.Gen[Pos[i]])
            Self.Gen.append(SolMutada)

    def SelGen(Self):
        Total = Self.tamPOB + Self.NumHijos + Self.NumMutaciones
        Beneficios = []

        for i in range(int(Total)):
            Beneficios.append(AGTSP.Beneficio(Self,Self.Gen[i]))

        TotalMejores = int(Self.pSEL * Self.tamPOB)
        PosMejores = AGTSP.PosMejorMinimos(Self,Beneficios,int(TotalMejores))


        for i in range(int(TotalMejores)):
             Self.Gen[i] = Self.Gen[PosMejores[i]]



        Faltan = int(Self.tamPOB - TotalMejores)
        PosFaltan = AGTSP.GetPosNoRep(Self, Self.tamPOB, Total, Faltan)
        Pos = TotalMejores

        for i in range(int(Faltan)):
            Self.Gen[Pos] = Self.Gen[PosFaltan[i]]
            Pos = Pos + 1

    def EjecutarAG(Self):
        MejorSol = []
        AGTSP.ConstruirPobInicial(Self)
        for i in range(Self.iterMAX):
            AGTSP.CruzarGen(Self)
            AGTSP.MutarGen(Self)
            AGTSP.SelGen(Self)

        MejorSol = Self.Gen[0]

        BeneficioMejorSol = AGTSP.Beneficio(Self,MejorSol)
        return MejorSol, AGTSP.Beneficio(Self,MejorSol)



#instancia
Matriz=np.array([[0, 7, 9, 8, 20],
                 [7, 0, 10, 4, 11],
                 [9, 10, 0, 15, 5],
                 [8, 4, 15, 0, 17],
                 [20, 11, 5, 17, 0]])


tamPOB = 500
iterMAX = 200
pMUTAR = 0.4
pCRUZAR = 0.6
pSEL = 0.8
PosInicial = 3


c = AGTSP(tamPOB, iterMAX, pMUTAR, pCRUZAR, pSEL, Matriz, PosInicial)

print(c.EjecutarAG())