import validmultiprocess
import validpool
import validthread
import time
import statistics

Tmutliprocess = []
Tpool = []
Tthread = []


if __name__ == '__main__':
    
    try:
        X = int(input("nombre de tests: "))
        for i in range(X):
            #multiprocess
            start = time.perf_counter()
            validmultiprocess.main()
            end = time.perf_counter()
            Tmutliprocess.append(round(end - start, 2))
            print(f"Tasks ended in {round(end - start, 2)} second(s)")

            #pool
            start = time.perf_counter()
            validpool.main()
            end = time.perf_counter()
            Tpool.append(round(end - start, 2))
            print(f"Tasks ended in {round(end - start, 2)} second(s)")

            #thread
            start = time.perf_counter()
            validthread.main()
            end = time.perf_counter()
            Tthread.append(round(end - start, 2))
            print(f"Tasks ended in {round(end - start, 2)} second(s)")
       

    except ValueError:
        print("Veuillez entrer un nombre entier")

    print(f"Temps moyen de téléchargement avec multiprocess: {statistics.fmean(Tmutliprocess)} secondes")
    print(f"Temps moyen de téléchargement avec pool: {round(statistics.fmean(Tpool),2)} secondes")
    print(f"Temps moyen de téléchargement avec thread: {statistics.fmean(Tthread)} secondes")

    
