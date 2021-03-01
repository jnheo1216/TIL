import 'package:flutter/material.dart';
import 'package:contacts_service/contacts_service.dart';  // 주소록 데이터에 접근하기 위한 패키지
import 'package:permission_handler/permission_handler.dart';  // 권한 요청을 앱키면 하게 해주는 패키지
import 'page_contact_detail.dart';
import 'page_contact_list.dart';

void main() => runApp(ContactDemoV3());

class ContactDemoV3 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: ContactListPage(),
      onGenerateRoute: (RouteSettings settings) {
        if (ContactDetailPage.routeName == settings.name) {
          Contact c = settings.arguments;
          return MaterialPageRoute(
              builder: (context) => ContactDetailPage(c));
        }
        return _noWay;
      });
  }

  final MaterialPageRoute _noWay = MaterialPageRoute(
    builder: (_) => Scaffold(
      body: Center(
        child: Text('경로가 없습니다.'),
      ),
    ),
  );
}
