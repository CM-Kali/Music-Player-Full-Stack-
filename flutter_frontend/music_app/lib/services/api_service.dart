import 'dart:convert';
import 'package:http/http.dart' as http;
import '../../models/song_model.dart';

class ApiService {
  // Your PC IP address
  static const String baseUrl = 'http://192.168.10.8:8000';

  Future<List<Song>> fetchSongs() async {
    try {
      final response = await http.get(Uri.parse('$baseUrl/songs'));

      if (response.statusCode == 200) {
        List<dynamic> jsonData = json.decode(response.body);
        return jsonData.map((song) => Song.fromJson(song)).toList();
      } else {
        throw Exception('Failed to load songs');
      }
    } catch (e) {
      throw Exception('Error fetching songs: $e');
    }
  }
}