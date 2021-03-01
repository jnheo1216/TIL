import 'package:flutter/material.dart';
import 'package:contacts_service/contacts_service.dart';  // 주소록 데이터에 접근하기 위한 패키지
import 'package:permission_handler/permission_handler.dart';  // 권한 요청을 앱키면 하게 해주는 패키지

class ContactDetailPage extends StatelessWidget {
  static const String routeName = '/contact';

  ContactDetailPage(this._contact);

  final Contact _contact;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(_contact.displayName ?? "")),
      body: ListView(
        children: <Widget>[
          ListTile(
            title: Text('Name'),
            trailing: Text(_contact.givenName ?? ""),
          ),
          ListTile(
            title: Text('Phones'),
            trailing: Text(
              _contact.phones.isNotEmpty ? _contact.phones.first.value : ""),
          ),
          ListTile(
            title: Text('Emails'),
            trailing: Text(
              _contact.emails.isNotEmpty ? _contact.emails.first.value : ""),
          ),
        ],
      ),
    );
  }
}