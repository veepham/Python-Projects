from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# Render Home page
def home(request):
    form = TransactionForm(data=request.POST or None)  # retrieve transaction form
    if request.method == 'POST':
        pk = request.POST['account']  # if form is submitted, retrieve which acct user wants to view
        return balance(request, pk)  # call balance function to render Balance sheet
    content = {'form': form}
    return render(request, 'checkbook/index.html', content)


# Render Create New Account page
def create_account(request):
    form = AccountForm(data=request.POST or None)  # Retrieve Account Form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    content = {'form': form}
    return render(request, 'checkbook/CreateNewAccount.html', content)


# Render Balance page
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)  # retrieve the request acct using primary key
    transactions = Transaction.Transactions.filter(account=pk)  # retrieve all of acct's transactions
    current_total = account.initial_deposit  # acct total variable
    table_contents = {}
    for t in transactions:  # loop thru transactions and determine if deposit or withdrawal
        if t.type == 'Deposit':
            current_total += t.amount
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# Render Transaction page
def transaction(request):
    form = TransactionForm(data=request.POST or None)  # Retrieve Account Form
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account']
            form.save()
            return balance(request, pk)
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
