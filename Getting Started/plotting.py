#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 14:20:56 2023

@author: laxman
"""

"""PLOTTING AND MORE ABOUT CLASSES"""

"""Plotting Using Matplotlib"""
# plt.sourceforge.net/users/index.html

import matplotlib.pyplot as plt 
plt.plot([1,2,3,4],[3,7,4,2])

plt.figure(1) # create figure 1
plt.plot([1,2,3,4],[2,3,4,5]) # draw on figure 1
plt.figure(2) # create figure 2
plt.plot([1,2,3,4],[5,6,1,4]) # draw on figure 2
plt.savefig('Fig-2') # save figure 2
plt.figure(1) # go back to working on figure 1.
plt.plot([4,10,13,23]) # draw on figure 1
plt.savefig('fig-1') # save figure 1

# compounded principal
principal = 10000
rate  = 0.05
value = []
years = 20 
for i in range(years+1):
    value.append(principal)
    principal +=principal*rate 
plt.plot(value)
plt.title("5% growth, Compounded anually")
plt.xlabel("years of compounding")
plt.ylabel("Value of Principal ($)")

# plt.sourceforge.net/users/index.html

plt.plot(value,'ko')
plt.title("5% growth, Compounded anually")
plt.xlabel("years of compounding")
plt.ylabel("Value of Principal ($)")

#### combined 
plt.plot(value,'ko')
plt.plot(value)
plt.title("5% growth, Compounded anually")
plt.xlabel("years of compounding")
plt.ylabel("Value of Principal ($)")

### example 
principal = 10000 #initial investment
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate
plt.plot(values, '-y', linewidth = 20)
plt.title('5% Growth, Compounded Annually',
fontsize = 'xx-large')
plt.xlabel('Years of Compounding', fontsize = 'x-small')
plt.ylabel('Value of Principal ($)')

#There are an enormous number of rcParams settings. A complete list can be 
#found at: http://plt.org/users/customizing.html

# http://plt.org/users/style_sheets.html#style-sheets

"""rcParams is a dictionary-like object in the matplotlib library that stores 
the default parameters used for creating and displaying plots. It contains a 
large number of parameters that control the appearance and behavior of various 
plot elements such as font sizes, line widths, colors, axes limits, and more.
"""
"""The values used in most of the remaining examples in this book were set 
with the code"""

# set line-width
plt.rcParams['lines.linewidth'] = 4
# set font-size for titles
plt.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
plt.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
plt.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
plt.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
plt.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
plt.rcParams['ytick.major.size'] = 7
#set size of markers, e.g., circles representing points
plt.rcParams['lines.markersize'] = 10
#set number of times marker is shown when displaying legend
plt.rcParams['legend.numpoints'] = 1
#Set size of type in legend
plt.rcParams['legend.fontsize'] = 14

"""Plotting Mortgages, an Extended Example"""

import matplotlib.pyplot as plt
import numpy as np
def findPayment(loan, r, m):
    """Assumes: loan and r are floats, m an int
    Returns the monthly payment for a mortgage of size
    loan at a monthly rate of r for m months"""
    return loan*((r*(1+r)**m)/((1+r)**m - 1))
class Mortgage(object):
    """Abstract class for building different kinds of mortgages"""
    def __init__(self, loan, annRate, months):
        self.loan = loan
        self.annRate = annRate
        self.month = months
        self.rate = annRate/12.0
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None # descrption of mortgage
        
    def make_paymennt(self):
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1]*self.rate
        self.outstanding.append(self.outstanding[-1]-reduction)
        
    def get_total_paid(self):
        return sum(self.paid)
    
    def __str__(self):
        return self.legend

    def plot_payments(self, style):
        plt.plot(self.paid[1:],style,label = self.legend)
        
    def plot_balance(self, style):
        plt.plot(self.outstanding, style, label = self.legend)
        
    def plot_tot_pd(self,style):
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        plt.plot(totPd,style, label = self.legend)
        
    def plot_net(self, style):
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
            equityAcquired = np.array([self.loan] * \
                                         len(self.outstanding))
            equityAcquired = equityAcquired - \
                    np.array(self.outstanding)
            net = plt.array(totPd) - equityAcquired
            plt.plot(net, style, label = self.legend)

class Fixed(Mortgage):
    def __init__(self, loan, r , months):
        Mortgage.__init__(self, loan, r, months)
        self._legend = f'Fixed, {r*100:.1f}%'
        
    def make_payment(self):
        if len(self._paid) ==self._teaser_momnths +1:
            self._rate = self.nextRate
            self._payment = findPayment(self._outstanding[-1],
                                    self._rate,
                                    self._months - self._teaser_months)
        Mortgage.make_payment(self)
        
class Fixed_with_pts(Mortgage):
    def __init__(self, loan, r, months, pts):
        self._pts = pts 
        self._paid = [loan*(pts/100)]
        self._legend = f'Fixed, {r*100:.1f}%, {pts} poits'
        
class Two_rate(Mortgage):
    def __init__(self, loan, r, months, teaser_rate, teaser_months):
        Mortgage.__init__(self, loan, teaser_rate, months)
        self._teaser_months = teaser_months
        self._teaser_rate = teaser_rate
        self._nextRate = r/12
        self._legend = (f'{100*teaser_rate:.1f}% for' +
                        f'{self._teaser_months} months, then {100*r:.1f}%')
        
    def make_payment(self):
        if len(self._paid) ==self._teaser_momnths +1:
            self._rate = self.nextRate
            self._payment = findPayment(self._outstanding[-1],
                                    self._rate,
                                    self._months - self._teaser_months)
        Mortgage.make_payment(self)
            
def compare_mortgage(amt, years, fixed_rate, pts, pts_rate,
                     var_rate1, var_rate2, var_months):
    tot_months = years*12
    fixed1  = Fixed(amt, fixed_rate, tot_months)
    fixed2 =  Fixed_with_pts(amt, pts_rate, tot_months,pts)
    two_rate = Two_rate(amt, var_rate2, tot_months, var_rate1,var_months)
    morts = [fixed1,  fixed2, two_rate]
    for m in range(tot_months):
        for mort in morts:
            mort.make_payment()
    plot_mortgages(morts, amt)
    
def plot_mortgages(morts, amt):
    def label_plot(figure, title, x_label, y_label):
        plt.figure(figure)
        plt.title(title)
        plt.ylabel(y_label)
        plt.legend(loc = 'best')
    styles = ['k-','k-.','k:']
    # Give names to figure
    payments, cost, balance, net_cost = 0, 1, 2, 3
    for i in range(len(morts)):
        plt.figure(payments)
        morts[i].plot_payments(styles[i])
        plt.figure(cost)
        morts[i].plot_tot_pd(styles[i])
        plt.figure(balance)
        morts[i].plot_balance(styles[i])
        plt.figure(net_cost)
        morts.plot_net(styles[i])
    label_plot(payments,f'Monthly Payments of ${amt:,} Mortgages',
               'Months', 'Monthly Payments')
    label_plot(cost, f'Cash Outlay of $ {amt:,} Mortgages',
               'Months', 'Total Pyaments')
    label_plot(balance, f'Balance remaining of $ {amt:,}, Mortgages',
               'Months', "Remaining Loan Blance of $")
    label_plot(net_cost, f'Net Cost of ${amt:, } Mortgages',
               'Months', 'Payments - Equity $')

compare_mortgage(amt=200000, years=30, fixed_rate=0.07,
                  pts = 3.25, pts_rate=0.05, var_rate1=0.045,
                  var_rate2=0.095, var_months=48)


"""New STart"""
class Mortgage(object):
    """Abstract class for building different kinds of mortgages"""
    def __init__(self, loan, annRate, months):
        self.loan = loan
        self.rate = annRate/12.0
        self.months = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None #description of mortgage
    def makePayment(self):
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1]*self.rate
        self.outstanding.append(self.outstanding[-1] - reduction)
    def getTotalPaid(self):
        return sum(self.paid)
    def __str__(self):
        return self.legend
    def plotPayments(self, style):
        plt.plot(self.paid[1:], style, label = self.legend)
    def plotBalance(self, style):
            plt.plot(self.outstanding, style, label = self.legend)
    def plotTotPd(self, style):
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
            plt.plot(totPd, style, label = self.legend)
    def plotNet(self, style):
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        equityAcquired = np.array([self.loan] * \
                                     len(self.outstanding))
        equityAcquired = equityAcquired - \
                   np.array(self.outstanding)
        net = np.array(totPd) - equityAcquired
        plt.plot(net, style, label = self.legend)
        
class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(r*100) + '%'

class FixedWithPts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100.0)]
        self.legend = 'Fixed, ' + str(r*100) + '%, '\
            + str(pts) + ' points'
            
class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r/12.0
        self.legend = str(teaserRate*100)\
            + '% for ' + str(self.teaserMonths)\
                + ' months, then ' + str(r*100) + '%'
                
    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.outstanding[-1],
                                       self.rate,
                                       self.months - self.teaserMonths)
            Mortgage.makePayment(self)
            
def compareMortgages(amt, years, fixedRate, pts, ptsRate,
                     varRate1, varRate2, varMonths):
    totMonths = years*12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
    morts = [fixed1, fixed2, twoRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
    plotMortgages(morts, amt)
    
def plotMortgages(morts, amt):
    def labelPlot(figure, title, xLabel, yLabel):
        plt.figure(figure)
        plt.title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.legend(loc = 'best')
    styles = ['k-', 'k-.', 'k:']
    #Give names to figure numbers
    payments, cost, balance, netCost = 0, 1, 2, 3
    for i in range(len(morts)):
        plt.figure(payments)
        morts[i].plotPayments(styles[i])
        plt.figure(cost)
        morts[i].plotTotPd(styles[i])
        plt.figure(balance)
        morts[i].plotBalance(styles[i])
        plt.figure(netCost)
        morts[i].plotNet(styles[i])
    labelPlot(payments, 'Monthly Payments of $' + str(amt) +
              ' Mortgages', 'Months', 'Monthly Payments')
    labelPlot(cost, 'Cash Outlay of $' + str(amt) +
              ' Mortgages', 'Months', 'Total Payments')
    labelPlot(balance, 'Balance Remaining of $' + str(amt) +
              ' Mortgages', 'Months', 'Remaining Loan Balance of $')
    labelPlot(netCost, 'Net Cost of $' + str(amt) + ' Mortgages',
              'Months', 'Payments - Equity $')
compareMortgages(amt=200000, years=30, fixedRate=0.07,
                 pts = 3.25, ptsRate=0.05,
                 varRate1=0.045, varRate2=0.095, varMonths=48)

