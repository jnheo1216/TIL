import 'package:flutter/material.dart';

void main() {
  runApp(TextDemo());
}

class TextDemo extends StatelessWidget {
  // This widget is the root of your application.
  static const String _title = 'Text 위젯 데모';
  static const String _name = ' 허 진 녕 ';
  static const String _longText = ' 플러터는 구글이 개발한 오픈소스 모바일 어플리케이션 개발 프레임워크다.';

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: _title,
      home: Scaffold(
        appBar: AppBar(title: Text(_title)),
        body: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Text('단순 텍스트 표시'), // 심플텍스트
            Text(
              'Styled Text with ${_name}',  // styled text
              style: TextStyle(
                color: Colors.black,
                fontSize: 20.0, //dp
                background: Paint()
                  ..color = Color(0xFFDCEDC8)
                  ..style = PaintingStyle.fill,
                fontWeight: FontWeight.bold),
            ),
            Text(
              _longText,
              overflow: TextOverflow.ellipsis, // 텍스트 오버플로우
            )
          ],
        ),
      ),
    );
  }
}
