package leetcode

type Bank struct {
	balance []int64
	n       int
}

func Constructor(balance []int64) Bank {
	return Bank{
		balance,
		len(balance),
	}
}

func (this *Bank) check(account int) bool {
	return 0 < account && account <= this.n
}

func (this *Bank) Transfer(account1 int, account2 int, money int64) bool {
	if !(this.check(account1) && this.check(account2)) {
		return false
	}

	if this.balance[account1-1] < money {
		return false
	}

	this.balance[account1-1] -= money
	this.balance[account2-1] += money

	return true
}

func (this *Bank) Deposit(account int, money int64) bool {
	if !this.check(account) {
		return false
	}

	this.balance[account-1] += money

	return true
}

func (this *Bank) Withdraw(account int, money int64) bool {
	if !this.check(account) || this.balance[account-1] < money {
		return false
	}

	this.balance[account-1] -= money

	return true
}

/**
 * Your Bank object will be instantiated and called as such:
 * obj := Constructor(balance);
 * param_1 := obj.Transfer(account1,account2,money);
 * param_2 := obj.Deposit(account,money);
 * param_3 := obj.Withdraw(account,money);
 */
