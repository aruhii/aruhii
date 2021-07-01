import 'package:flutter/material.dart';
import '../models/transaction.dart';

class TransactionOutput extends StatefulWidget {
  @override
  _TransactionOutputState createState() => _TransactionOutputState();
}

class _TransactionOutputState extends State<TransactionOutput> {
  final List<Transaction> _userTransactions = [
    Transaction(
      title: "Food",
      amount: 16.99,
      id: "20210331",
      date: DateTime.now(),
    ),
    Transaction(
      title: "Phone",
      amount: 100.00,
      id: "20200410",
      date: DateTime.now(),
    )
  ];

  @override
  Widget build(BuildContext context) {
    return Column();
  }
}
