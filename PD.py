import requests
import json
class Produkts:
    def __init__(self, nosaukums, cena, apraksts):
        self.nosaukums = nosaukums
        self.cena = cena
        self.apraksts = apraksts

    def get_nosaukums(self):
        return self.nosaukums
    def set_nosaukums(self, n):
        self.nosaukums = n

    def get_cena(self):
        return self.cena
    def set_cena(self, n):
        self.cena = n


    def get_apraksts(self):
        return self.apraksts
    def set_apraksts(self, n):
        self.apraksts = n


class Elektronika(Produkts):
    def __init__(self, nosaukums, cena, apraksts,jauda):
        super().__init__(nosaukums, cena, apraksts)
        self.jauda = jauda
    def get_jauda(self):
        return self.jauda
    def set_jauda(self, n):
        self.jauda = n


class Apgerbs(Produkts):
    def __init__(self, nosaukums, cena, apraksts,izmers):
        super().__init__(nosaukums, cena, apraksts)
        self.izmers = izmers
    def get_jauda(self):
        return self.izmers
    def set_jauda(self, n):
        self.izmers = n

class Gramata(Produkts):  
    def __init__(self, nosaukums, cena, apraksts,lapaspuses):
        super().__init__(nosaukums, cena, apraksts)
        self.lapaspuses = lapaspuses
    def get_jauda(self):
        return self.lapaspuses
    def set_jauda(self, n):
        self.lapaspuses = n


class Grozs:
    def __init__(self):
        self.saturs = []

    def pievienot(self,prece,skaits=1):
        ok = True
        for i in range(len(self.saturs)):
            (p,s) = self.saturs[i]
            if p == prece:
                s = s+1
                self.saturs[i] = (p,s)
                ok = False
        if ok:
            self.saturs.append((prece,skaits))

    def dzest(self,prece):
      
        for i in range(len(self.saturs)):
            (p,s) = self.saturs[i]
            
            if p == prece:
                s = s-1
                self.saturs[i] = (p,s)
                k = (p,s)
                if s == 0:
                   self.saturs.remove(k) 
        


                
            
            

    def kopums(self):
        if self.saturs == []:
            print("Grozs ir tukšs")
        else:
            print("Groza saturs:")
            count =1 
            for i in range(len(self.saturs)):

                if self.saturs[i][1] > 0:
                    
                    print("{}: nosaukums: {} cena: {} apraksts: {}".format(count,self.saturs[i][0].nosaukums, self.saturs[i][0].cena,self.saturs[i][0].apraksts))
                    count = count +  1


    def kopeja_vertiba(self,kurss):
        def vertiba_sum(self):
            total = 0
            for i in range(len(self.saturs)):
                (p,s) = self.saturs[i]
                total += p.get_cena()*s
            return total
        if kurss == 'EUR':
            vertiba = vertiba_sum(self)
            print('Kopējā vērtība: {}'.format(vertiba))
        else:
            api = 'http://open.er-api.com/v6/latest/EUR'
            response = requests.get(api)
            if response.status_code == 200:
                # Request was successful
          
                data = response.text
                data = json.loads(data)
                reiznatajs = data['rates'][kurss]
                vertiba = vertiba_sum(self)
                print('Kopējā vērtība: {}'.format(vertiba*reiznatajs))
            else:
                # Request failed
                print("Neizdevās savienoties ar serveri:", response.status_code)

        
    
def main():
    g = Grozs()
    tehnika = Elektronika('iphone',500,'no Apple',1000)
    kanceleja = Gramata('Sola',5,'no G. Janovska',300)
    virsdrebes = Apgerbs('t-krekls',10,'no Pakistanas','XL')
    g.pievienot(tehnika)
    g.pievienot(kanceleja)
    g.pievienot(virsdrebes)
    g.kopums()
    g.dzest(tehnika)
    g.kopums()
    g.kopeja_vertiba('EUR')

if __name__ =='__main__':
    main()