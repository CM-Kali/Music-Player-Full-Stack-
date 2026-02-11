// import 'package:flutter/material.dart';
// import 'package:music_app/player_screen.dart';
// import 'song_model.dart';
// import 'api_service.dart';
// class HomeScreen extends StatefulWidget {
//   @override
//   State<HomeScreen> createState() => _HomeScreenState();
// }
//
// class _HomeScreenState extends State<HomeScreen> {
//   late Future<List<Song>> songs;
//
//   @override
//   void initState() {
//     songs = ApiService.fetchSongs();
//     super.initState();
//   }
//
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(title: Text("Mini Music")),
//       body: FutureBuilder(
//         future: songs,
//         builder: (context, snapshot) {
//           if (!snapshot.hasData) return Center(child: CircularProgressIndicator());
//           final list = snapshot.data!;
//           return ListView.builder(
//             itemCount: list.length,
//             itemBuilder: (context, index) {
//               return ListTile(
//                 leading: Icon(Icons.music_note),
//                 title: Text(list[index].title),
//                 subtitle: Text(list[index].artist),
//                 onTap: () {
//                   Navigator.push(
//                     context,
//                     MaterialPageRoute(
//                       builder: (_) => PlayerScreen(song: list[index]),
//                     ),
//                   );
//                 },
//               );
//             },
//           );
//         },
//       ),
//     );
//   }
// }
