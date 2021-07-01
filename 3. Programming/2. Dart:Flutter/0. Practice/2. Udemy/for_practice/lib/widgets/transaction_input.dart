import 'package:flutter/material.dart';

class TransactionInput extends StatelessWidget {
  final titleController = TextEditingController();
  final amountController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Card(
        elevation: 5,
        child: Column(
          children: [
            Container(
              width: double.infinity,
              child: Text("Put in!"),
              color: Colors.blue,
            ),
            TextField(
              decoration: InputDecoration(labelText: "Title"),
              controller: titleController,
            ),
            TextField(
              decoration: InputDecoration(labelText: "Title"),
              controller: amountController,
            ),
            FlatButton(
              onPressed: () {},
              child: Text(
                "Add Transaction",
                textAlign: TextAlign.end,
              ),
            ),
          ],
        ));
  }
}
