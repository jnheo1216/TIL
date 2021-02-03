import 'package:flutter/material.dart';
import 'package:contacts_service/contacts_service.dart';  // 주소록 데이터에 접근하기 위한 패키지
import 'package:permission_handler/permission_handler.dart';  // 권한 요청을 앱키면 하게 해주는 패키지

void main() => runApp(ListViewDymamicApp());


class ListViewDymamicApp extends StatelessWidget {
  static const String _title = '동적 리스트뷰 위젯 데모 주소록';
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: _title,
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(title: Text(_title)),
        body: ContactListPage(),
      ),
    );
  }
}

class ContactListPage extends StatefulWidget {
  @override
  _ContactListPageState createState() => _ContactListPageState();   // stateful
}

class _ContactListPageState extends State<ContactListPage> {
  Iterable<Contact> _contacts;

  @override
  void initState() {
    super.initState();
    _checkPermissions();   // 먼저 권한을 확인해주는 메서드를 호출
  }

  _checkPermissions() async {   // 사용자의 선택을 기다려야 하므로 비동기
    await PermissionHandler().requestPermissions([PermissionGroup.contacts]);  // 여기에 넣은 인자가 바로 xml에서 선언한 그 권한임
    refreshContacts();   // 권한을 획득한 후, contact_service패키지의 ContactService, getContacts 를 호출함
  }

  refreshContacts() async {
    Iterable<Contact> contacts =
        await ContactsService.getContacts(withThumbnails: false);  // withthumbnail : 썸네일 소환을 막아줘서 속도 업
    setState(() {
      _contacts = contacts;  // 로딩 완료시 contacts 변수 갱신
    });
  }

  @override
  Widget build(BuildContext context) {
    return _contacts != null   // 주소록을 부르는 시간이 있기 때문에 null 값을 넣어둠
        ? ListView.builder(itemCount: _contacts.length, itemBuilder: _buildRow)  // 목록의 개수지정 itemcount로, 각 행의 내용은 itembuilder로 분리
        : Center(child: CircularProgressIndicator());  // 주소록 로딩 전에는 이걸 보여주는 거임
  }

  Widget _buildRow(BuildContext context, int i) {
    Contact c = _contacts.elementAt(i);
    return ListTile(   // 이 위젯으로 리스트의 각 행을 표시할수있다.
      leading: (c.avatar != null && c.avatar.length > 0)
          ? CircleAvatar(backgroundImage: MemoryImage(c.avatar))   // 있다면 주소록에 있는 사진(avartar)을 표시하거나
          : CircleAvatar(child: Text(c.initials())),   // 아니면 그 첫번째 글자로 표시
      title: Text(c.displayName ?? ""),  // 주소록의 표시 이름으로 title, 없을시 ""공백
    );
  }
}
