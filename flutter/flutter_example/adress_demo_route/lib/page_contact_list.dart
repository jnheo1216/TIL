import 'package:flutter/material.dart';
import 'package:contacts_service/contacts_service.dart';  // 주소록 데이터에 접근하기 위한 패키지
import 'package:permission_handler/permission_handler.dart';  // 권한 요청을 앱키면 하게 해주는 패키지
import 'page_contact_detail.dart';

class ContactListPage extends StatefulWidget {
  @override
  _ContactListPageState createState() => _ContactListPageState();
}

class _ContactListPageState extends State<ContactListPage> {
  Iterable<Contact> _contacts;

  @override
  void initState() {
    super.initState();
    refreshContacts();
  }

  refreshContacts() async {
    Iterable<Contact> contacts =
        await ContactsService.getContacts(withThumbnails: false);
    setState(() {
      _contacts = contacts;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('주소록 데모')),
      body: _contacts != null
          ? ListView.builder(
              itemCount: _contacts.length,
              itemBuilder: _buildRow,
      )
          : Center(child: CircularProgressIndicator()));
  }

  @override
  Widget _buildRow(BuildContext context, int i) {
    Contact c = _contacts.elementAt(i);
    return ListTile(
      leading: (c.avatar != null && c.avatar.length > 0)
          ? CircleAvatar(backgroundImage: MemoryImage(c.avatar))
          : CircleAvatar(child: Text(c.initials())),
      title: Text(c.displayName ?? ""),
      onTap: () => Navigator.pushNamed(context, ContactDetailPage.routeName,
          arguments: c),
    );
  }
}