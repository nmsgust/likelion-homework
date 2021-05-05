from django.shortcuts import render


def index(request):
    return render(request, 'index.html') 

def result(request):
    sentence = request.POST.get('sentence')

    words = sentence.split()

    word_counts = {}
    #딕셔너리가 비어있음 

    for word in words:
        if word in word_counts: # 이 단어가 워드카운터에 있으면 +1을 해줘 
            word_counts[word] += 1
        else:
            word_counts[word] = 1 # word라는 키로 숫자 하나만 넣어줘 



    word_counts_list = list(word_counts.items())
    word_counts_list.sort(key = lambda t : -t[1]) #정렬을 할때 난 1번째에 있는 걸 정렬의 기준으로 삼고잎어 
#sort가 기본적으로 오름차순 정렬이기 때문에 - 붙여서 바꿈
#lambda라는 함수는 짧은 함수
#t는 다른영어여도 가능


    response = {
        'word_counts': word_counts_list
    } #요청을 response라는 딕셔너리 안에서 워드 카운트는 워드 카운트야 라고 보냄 

    return render(request, 'result.html', response) #response응답을 담아줘 
    # result 라는 함수는 어떤 요청이 들어오면 result.html을 render(화면에 보여줘)

