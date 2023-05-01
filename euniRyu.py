
example = [[1,2,3],[4,[5,6]],7,[8,9]];

#flatten이라는 것 자체가 재귀적으로 처리해 배열의 값들을 하나의 배열로 펼치는 것.
def flatten(data): 

  #변수 하나 생성
  output=[]
  #파라미터 data의 배열을 순회하며 해당 값이 리스트인지 아닌지 판별
  for item in data:
    if type(item)==list:
      #재귀적으로 처리
      #해당 값이 리스트면 자기 자신인 함수를 다시 호출해 한번더 순회하도록 함
      output+=flatten(item)
    else:
      #배열이 아닐 경우 해당 값을 output에 추가
      output.append(item)
  #최종적으로 하나의 배열안에 모든 값들이 들어있는게 반환됨
  return output

print(flatten(example))