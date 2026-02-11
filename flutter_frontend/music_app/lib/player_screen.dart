import 'package:flutter/material.dart';
import 'package:just_audio/just_audio.dart';
import 'song_model.dart';

class PlayerScreen extends StatefulWidget {
  final Song song;
  PlayerScreen({required this.song});

  @override
  State<PlayerScreen> createState() => _PlayerScreenState();
}

class _PlayerScreenState extends State<PlayerScreen> {
  late final AudioPlayer player;
  late Future<void> _playerFuture;
  bool isPlaying = false;

  @override
  void initState() {
    super.initState();
    player = AudioPlayer();
    _playerFuture = player.setUrl(widget.song.audioUrl); // async loading
  }

  @override
  void dispose() {
    player.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(widget.song.title)),
      body: FutureBuilder(
        future: _playerFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState != ConnectionState.done) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text("Error loading audio"));
          }

          return Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(Icons.album, size: 120),
              SizedBox(height: 20),
              Text(widget.song.artist),
              SizedBox(height: 20),
              IconButton(
                icon: Icon(isPlaying ? Icons.pause : Icons.play_arrow, size: 50),
                onPressed: () async {
                  if (isPlaying) {
                    await player.pause();
                  } else {
                    await player.play();
                  }
                  setState(() => isPlaying = !isPlaying);
                },
              ),
            ],
          );
        },
      ),
    );
  }
}
