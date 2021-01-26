import 'dart:io';
import 'dart:math';
import 'dart:convert';

void main() {

  /////////////////////////////////////////////////////////////////

  // dart:core 패키지
  // 보통 우리가 써왔던 기본적인 것들. import 안해도 자동으로 적용된다.
  print('hello world!');  

  int num1 = 5000;
  print(num1);
  String num1str = num1.toString();  // 정수를 문자열로
  print(num1str);

  String str1 = '34.24';
  print(str1);
  double str1num = double.parse(str1);  // 형을 잘 맞춰줘야함. 더블은 더블끼리 인트는 인트끼리
  print(str1num);

  //////////////////////////////////////////////////////////
  
  // dart:io 패키지
  // 입출력 관장하는 패키지
  stdout.write('Enter name? ');  // 프린트와 같음 이건
  String input = stdin.readLineSync();

  print('hello ${input}');

  /////////////////////////////////////////////////////////////
  // dart:math 패키지
  // 최대 최소 난수 등등등 

  List<int> nums = [100, 200, 300, 400, 2500];
  int maxValue = max(nums[0], nums[1]);
  int minValue = min(nums[2], nums[3]);  // 최대최소
  print(maxValue);
  print(minValue);

  double sqaureRooted = sqrt(nums[4]);  // 제곱근
  print(sqaureRooted);

  Random rand = Random();
  int randomNumber = rand.nextInt(10);
  print(randomNumber);

  /////////////////////////////////////////////////////////////
  
  // dart:convert 패키지
  // json 파일 받을때 씀 
  String jsonStr = """
  {"basket" : {
    "apple" : 50, 
    "banana" : 10,
    "grape" : 5
    }  
  }
  """;
  print(jsonStr);

  Map json = jsonDecode(jsonStr);
  Map basket = json['basket'];
  int apple = basket['apple'];
  int banana = basket['banana'];
  int grape = basket['grape'];

  print(apple);
  print(banana);
  print(grape);

  // String jsonfile = File('filename.json').readAsStringSync(); // json파일 읽어오기
  // Map my_json = jsonDecode(jsonfile);

  // File('new_json.json').writeAsStringSync(jsonEncode(basket)); // json파일 쓰기

}

