from concurrent.futures import ThreadPoolExecutor, as_completed
import data.getData as getData
def concurrentE(syUrl,pwd,max_workers,work):
    listDataSuccess = []
    listDataFalse =[]
    tasks = getData.getSY(syUrl)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交任务
        futures = [executor.submit(work, sy, pwd) for sy in tasks]
        # 等待所有任务完成
        for future in as_completed(futures):
            try:
                result = future.result()
                listDataSuccess.append(result)
                # listDataSuccess.append(result[:][:2])
                if result[2] == 0:
                    listDataFalse.append(result[:][:1])
            except Exception as e:
                print(f"Error occurred during execution: {e}")
    getData.saveData(listDataSuccess)
    getData.saveFalData(listDataFalse)
    print('Finished executing Selenium sessions')


