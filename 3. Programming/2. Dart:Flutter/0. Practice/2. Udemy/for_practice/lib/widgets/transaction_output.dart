import 'package:flutter/material.dart';
import '../models/transaction.dart';
import 'transaction_input.dart';

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

  void addNewTransaction(String title, double amount) {
    Transaction tmp_transaction = Transaction(
      title: title,
      amount: amount,
      id: DateTime.now().toString(),
      date: DateTime.now(),
    );
    _userTransactions.add(tmp_transaction);
  }

  @override
  Widget build(BuildContext context) {
    return Column();
  }
}
