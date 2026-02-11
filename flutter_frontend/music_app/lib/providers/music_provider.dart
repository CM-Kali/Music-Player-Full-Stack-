import 'package:flutter/foundation.dart';
import 'package:just_audio/just_audio.dart';
import '../models/song_model.dart';
import '../services/api_service.dart';

class MusicProvider extends ChangeNotifier {
  final ApiService _apiService = ApiService();
  final AudioPlayer _audioPlayer = AudioPlayer();

  List<Song> _songs = [];
  Song? _currentSong;
  bool _isPlaying = false;
  bool _isLoading = false;
  Duration _position = Duration.zero;
  Duration _duration = Duration.zero;

  List<Song> get songs => _songs;
  Song? get currentSong => _currentSong;
  bool get isPlaying => _isPlaying;
  bool get isLoading => _isLoading;
  Duration get position => _position;
  Duration get duration => _duration;
  AudioPlayer get audioPlayer => _audioPlayer;

  MusicProvider() {
    _init();
  }

  void _init() {
    _audioPlayer.positionStream.listen((pos) {
      _position = pos;
      notifyListeners();
    });

    _audioPlayer.durationStream.listen((dur) {
      _duration = dur ?? Duration.zero;
      notifyListeners();
    });

    _audioPlayer.playerStateStream.listen((state) {
      _isPlaying = state.playing;
      notifyListeners();
    });
  }

  Future<void> loadSongs() async {
    _isLoading = true;
    notifyListeners();

    try {
      _songs = await _apiService.fetchSongs();
    } catch (e) {
      debugPrint('Error loading songs: $e');
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<void> playSong(Song song) async {
    if (_currentSong?.id == song.id && _isPlaying) {
      await pause();
      return;
    }

    try {
      _currentSong = song;
      await _audioPlayer.setUrl(song.audioUrl);
      await _audioPlayer.play();
    } catch (e) {
      debugPrint('Error playing song: $e');
    }
  }

  Future<void> pause() async {
    await _audioPlayer.pause();
  }

  Future<void> resume() async {
    await _audioPlayer.play();
  }

  Future<void> seek(Duration position) async {
    await _audioPlayer.seek(position);
  }

  void playNext() {
    if (_currentSong == null || _songs.isEmpty) return;

    int currentIndex = _songs.indexWhere((s) => s.id == _currentSong!.id);
    if (currentIndex < _songs.length - 1) {
      playSong(_songs[currentIndex + 1]);
    }
  }

  void playPrevious() {
    if (_currentSong == null || _songs.isEmpty) return;

    int currentIndex = _songs.indexWhere((s) => s.id == _currentSong!.id);
    if (currentIndex > 0) {
      playSong(_songs[currentIndex - 1]);
    }
  }

  @override
  void dispose() {
    _audioPlayer.dispose();
    super.dispose();
  }
}