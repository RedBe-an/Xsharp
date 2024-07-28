## Xsharp 문법 요약

### 주석
- 한 줄 주석: `// This is comment!`
- 여러 줄 주석: 
  ```Xsharp
  /*
  This is multiline comment!
  awesome comment ;)
  */
  ```

### 변수
- Mutable 변수:
  ```Xsharp
  let a: String = "a";
  ```
- Constant 변수:
  ```Xsharp
  const B: String = "B";
  ```
- 섀도잉을 통한 타입 변경:
  ```Xsharp
  let a: String = "a";
  let a: Integer = 1; // 기존 변수 a를 새로운 Integer 타입으로 가림
  ```

### 타입
- `String`: 문자열
- `Integer`: 정수형
- `Float`: 부동 소수점 숫자
- `Tuple`: 변경 불가한 여러 타입의 조합 (예: `Tuple<Int | String>`)
- `Array`: 변경 가능한 배열 (예: `Array<Int | String>`)
- `Void`: 값이 없음 (예: 반환 값이 없는 함수)
- `Any`: 어떤 값이든 가능 (다른 모든 타입보다 상위)

### 함수
- 함수 정의:
  ```Xsharp
  func hello(name: String) -> void {
      print("hello, {name}!")
  }
  ```
- 메인 함수 예시:
  ```Xsharp
  func main() {
      print("here is! main function!")
      hello("world")
  }
  ```
- 매개변수 타입 명시 필요

### 제어문
- `for`문:
  ```Xsharp
  for char in characters {
      // 반복 내용
  }
  ```
- `while`문:
  ```Xsharp
  while condition {
      // 반복 내용
  }
  ```
- `loop`문 (값 반환 가능):
  ```Xsharp
  let a: Integer = loop {
      let counter: Integer = 0;

      counter += 1;

      if counter == 10 {
          break counter;
      }
  };
  ```

## 예제 정리

### 1. 변수와 타입 섀도잉
- 기존의 `String` 타입 변수를 `Integer` 값으로 재할당하면 오류 발생:
  ```Xsharp
  let a: String = "a";
  a = 1; // 오류 발생, String 타입에 Integer 값을 할당하려고 함
  ```
- 섀도잉을 통해 새로운 변수를 선언하여 기존 변수를 가림:
  ```Xsharp
  let a: String = "a";
  let a: Integer = 1; // 섀도잉을 통해 새로운 Integer 타입 변수 선언
  ```

### 2. 튜플과 배열 예제
- 튜플 예제:
  ```Xsharp
  const tuple: Tuple<Int | String> = ('1', 2, '3');
  ```
- 배열 예제:
  ```Xsharp
  let array: Array<Int | String> = ['1', 2, '3'];
  ```

### 3. `loop` 문에서 값 반환 예제
- `loop` 문을 통해 값을 반환하는 예제:
  ```Xsharp
  let a: Integer = loop {
      let counter: Integer = 0;

      counter += 1;

      if counter == 10 {
          break counter;
      }
  };
  ```

### 4. 타입 명시
- 모든 변수와 매개변수에 타입을 명시해야 함:
  ```Xsharp
  let name: String = "example";
  func greet(name: String) -> void {
      print("Hello, {name}!");
  }
  ```
