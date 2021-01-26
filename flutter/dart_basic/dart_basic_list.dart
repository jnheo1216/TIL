void main() {
  List<int> numbers = [100, 200, 300];
  List<int> numbers2 = [400, 500, 600];
  List<String> planets = ['earth', 'jupyter', 'venus', 'seturn'];

  print('numbers list ${numbers}');
  print('planets list ${planets}');

  for (String planet in planets) {
    print(planet);
  }

  List numbersplus = numbers + numbers2;
  print(numbersplus);

  ///////////////////////////////////////////////

  Set a = {100, 200, 300};
  Set b = {100, 200, 500, 1000};
  print('a union b ${a.union(b)}');  // 합집합
  print('a intersection b ${a.intersection(b)}');  // 교집합
  print('a difference b ${a.difference(b)}');  // 차집합

  ////////////////////////////////////////////
  
  Map<int, String> intMap = {0:'AAA', 1:'BBB', 2:'CCC'};  // 파이썬 딕셔너리 같다.
  print(intMap);
  intMap.update(1, (value) => 'DDD');
  print(intMap);

}