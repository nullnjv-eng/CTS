import time

Completions = []
Tasks = []
Sessions = []


def create_completion(
    key: int,
    datetime: int,
    response: str,
    stage: str,
    error: str,
    task: int
):
    Completions.append([key, datetime, response, stage, error, task])


def create_task(
    key: int,
    datetime: int,
    parameter: str,
    session: int,
    description: str,
    done: int
):
    Tasks.append([key, datetime, parameter, session, description, done])


def create_session(
    key: int,
    datetime: int,
    ip: str,
    locale: str,
    user_agent: str
):
    Sessions.append([key, datetime, ip, locale, user_agent])


def delete_universal(list_name, key):
    for i in range(len(list_name)):
        if list_name[i][0] == key:
            list_name.pop(i)


def get_all_writings_universal(list_name):
    return (list_name)


def get_one_writing_by_id_universal(list_name, key):
    for i in range(len(list_name)):
        if list_name[i][0] == key:
            return (list_name[i])


passed_selection_completions_keys = []
tasks_keys = []
selected_completions_tasks = []
joined_strings = []


def sub_a():
    for i in range(len(tasks_keys)):
        for j in range(len(selected_completions_tasks)):
            if tasks_keys[i] == selected_completions_tasks[j]:
                s1 = ""
                s2 = ""
                for ii in range(len(Tasks)):
                    if Tasks[ii][0] == tasks_keys[i]:
                        s1 = Tasks[ii]
                        break
                for jj in range(len(Completions)):
                    if Completions[jj][5] == selected_completions_tasks[j]:
                        s2 = Completions[jj]
                joined_strings.append(s1 + s2)


def additional_relating_algebra():
    for i in range(len(Completions)):
        if Completions[i][1] >= time.time() - 7 * 60:
            passed_selection_completions_keys.append(Completions[i][0])
    for i in range(len(Tasks)):
        tasks_keys.append(Tasks[i][0])
    for i in range(len(passed_selection_completions_keys)):
        for j in range(len(Completions)):
            if passed_selection_completions_keys[i] == Completions[j][0]:
                selected_completions_tasks.append(Completions[j][5])
    sub_a()
    for i in range(len(joined_strings)):
        a = joined_strings[i][8] + " " + joined_strings[i][4]
        b = " " + joined_strings[i][2]
        print (a + b)
    passed_selection_completions_keys = []
    tasks_keys = []
    selected_completions_tasks = []
    joined_strings = []


while True:
    command = input()
    exec(command)
