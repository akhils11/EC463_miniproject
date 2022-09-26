import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

Future<Map> fetchResponse(http.Client client, String username) async {
  final response = await client.get(Uri.parse('https://flask-r4i6lly44a-nn.a.run.app/?username=$username'));
  return parseResponse(response.body);
}

class Response {
  final String pfp;
  final double bot;
  final Map tweets;
  final Map sentiment;

  const Response({
    required this.pfp,
    required this.bot,
    required this.tweets,
    required this.sentiment,
  });

  factory Response.fromJson(Map<Map, dynamic> json) {
    return Response(
      pfp: json['tweepy']['image'] as String,
      bot: json['botometer']['cap']['universal'] as double,
      tweets: json['tweepy']['tweets'] as Map,
      sentiment: json['googlenlp'] as Map,
    );
  }
}

Map parseResponse(String responseBody) {
  final parsed = jsonDecode(responseBody);
  return parsed;
}

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.grey,
      ),
      home: const MyHomePage(title: 'Twitter Analytics'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final myController = TextEditingController();
  late Map response = {};
  bool showData = false;
  int numTweets = 0;

  final List<String> tweets = [];
  final List<String> topics = [];

  @override
  Widget build(BuildContext context) {
    final ButtonStyle style = ElevatedButton.styleFrom(textStyle: const TextStyle(fontSize: 20));
    return Scaffold(
      body: Container(
        child: ConstrainedBox(
          constraints: const BoxConstraints(maxHeight: 1000, maxWidth: 2560),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              ConstrainedBox(
                constraints: const BoxConstraints(maxHeight: 600, maxWidth: 2560),
                child: Row(
                  children: [
                    showData
                        ? Container(
                            alignment: Alignment.center,
                            padding: const EdgeInsets.symmetric(vertical: 50, horizontal: 100),
                            child: SizedBox(
                              height: 100,
                              width: 100,
                              child: FittedBox(
                                fit: BoxFit.fill,
                                child: Image.network(
                                  response['tweepy']['image'],
                                  filterQuality: FilterQuality.high,
                                ),
                              ),
                            ),
                          )
                        : const SizedBox(
                            height: 0,
                          ),
                    ConstrainedBox(
                      constraints: BoxConstraints(maxHeight: 1000, maxWidth: 700),
                      child: ListView.builder(
                        physics: const AlwaysScrollableScrollPhysics(),
                        scrollDirection: Axis.vertical,
                        shrinkWrap: true,
                        padding: const EdgeInsets.all(5),
                        itemCount: numTweets,
                        itemBuilder: (BuildContext context, int index) {
                          return Container(
                            child: Text(tweets[index]),
                          );
                        },
                      ),
                    ),
                    showData
                        ? Container(
                            alignment: Alignment.center,
                            padding: const EdgeInsets.symmetric(vertical: 20, horizontal: 30),
                            child: SizedBox(
                              height: 150,
                              width: 150,
                              child: Container(
                                child: Text("Botometer: ${((1 - response['botometer']['cap']['universal']) * 100).round()}%"),
                              ),
                            ),
                          )
                        : const SizedBox(
                            height: 0,
                          ),
                    showData
                        ? Container(
                            alignment: Alignment.center,
                            padding: const EdgeInsets.symmetric(vertical: 20, horizontal: 30),
                            child: SizedBox(
                              height: 150,
                              width: 150,
                              child: Container(
                                child: Text("Topics: ${topics}"),
                              ),
                            ),
                          )
                        : const SizedBox(
                            height: 0,
                          ),
                  ],
                ),
              ),
              Container(
                alignment: Alignment.center,
                padding: const EdgeInsets.symmetric(vertical: 20, horizontal: 50),
                child: TextField(
                  textInputAction: TextInputAction.newline,
                  controller: myController,
                  decoration: const InputDecoration(
                    border: OutlineInputBorder(),
                    hintText: 'Input a user\'s twitter handle',
                  ),
                ),
              ),
              ElevatedButton(
                style: style,
                child: const Text("Enter"),
                onPressed: () async {
                  response = await fetchResponse(http.Client(), myController.text);
                  numTweets = response['tweepy']['num_tweets'];
                  response['tweepy']['tweets'].forEach((k, v) => tweets.add(v['text']));

                  response['googlenlp'].forEach((k, v) => topics.add(v['classify']['categories'].toString()));
                  topics.toSet().toList();

                  print("Received Response");
                  setState(() {
                    showData = true;
                  });
                },
              )
            ],
          ),
        ),
      ),
    );
  }
}
