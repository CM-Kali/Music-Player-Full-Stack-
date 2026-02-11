import 'dart:convert';
import 'package:http/http.dart' as http;
import 'song_model.dart';

class ApiService {
  // Replace with your PC's IP and port
  static const String baseUrl = "http://192.168.10.8:8000";

  static Future<List<Song>> fetchSongs() async {
    final response = await http.get(Uri.parse("$baseUrl/songs"));

    if (response.statusCode != 200) {
      throw Exception("Failed to load songs: ${response.statusCode}");
    }

    final List data = json.decode(response.body);
    return data.map((e) => Song.fromJson(e)).toList();
  }
}
