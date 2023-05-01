
example = [[1,2,3],[4,[5,6]],7,[8,9]];

function flatten(data){
  let output = []; 

  data.forEach((value) => {
    if (Array.isArray(value)) {
      // 재귀적으로 처리
      //자기자신을 호출해 배열을 펼치는 작업이므로 전개 연산자 사용 必
      output.push(...flatten(value));
    }
    else{
      output.push(value);
    }
  });
  return output;
}

console.log(flatten(example));