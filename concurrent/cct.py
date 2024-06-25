from concurrent.futures import ThreadPoolExecutor, as_completed
import data.getData as getData


def concurrent_e(tasks, max_workers, work):
    list_data_success = []
    list_data_false = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交任务(多参数为 work ，a， b) work为方法名，data为任务数据
        futures = [executor.submit(work, data) for data in tasks]
        # 等待所有任务完成
        for future in as_completed(futures):
            try:
                result = future.result()
                list_data_success.append(result)
                # 每次io都保存一次数据避免发生异常产生中断
                getData.saveData(list_data_success)
                # listDataSuccess.append(result[:][:2])
                if result[2] == 0:
                    list_data_false.append(result[:][:1])
                    getData.saveFalData(list_data_false)
            except Exception as e:
                print(f"Error occurred during execution: {e}")
    print('Finished executing Selenium sessions')
