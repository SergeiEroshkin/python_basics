//
//  main.cpp
//  inventory
//
//  Created by Sergei Eroshkin on 12/4/16.
//  Copyright © 2016 Sergei Eroshkin. All rights reserved.
//

#include <iostream>
#include <map>
#include <thread>
#include <chrono>
#include <unistd.h>
using namespace std;

// Thread Timer Class for Maintaining Orders' Threads
class Timer {
public:
    typedef std::chrono::milliseconds Interval;
    typedef std::function<void(void)> Timeout;
    
    Timer(const Timeout &timeout);
    Timer(const Timeout &timeout, const Interval &interval, bool singleShot = true);
    
    void start(bool multiThread = false);
    void stop();
    
    bool running() const;
    
    void setSingleShot(bool singleShot);
    bool isSingleShot() const;
    
    void setInterval(const Interval &interval);
    const Interval &interval() const;
    
    void setTimeout(const Timeout &timeout);
    const Timeout &timeout() const;
    
private:
    std::thread _thread;
    
    bool _running = false;
    bool _isSingleShot = true;
    
    Interval _interval = Interval(0);
    Timeout _timeout = nullptr;
    
    void _temporize();
    void _sleepThenTimeout();
};

Timer::Timer(const Timeout &timeout)
: _timeout(timeout)
{
}

Timer::Timer(const Timer::Timeout &timeout,
             const Timer::Interval &interval,
             bool singleShot)
: _isSingleShot(singleShot),
_interval(interval),
_timeout(timeout)
{
}

void Timer::start(bool multiThread)
{
    if (this->running() == true)
        return;
    
    _running = true;
    
    if (multiThread == true) {
        _thread = std::thread(
                              &Timer::_temporize, this);
    }
    else{
        this->_temporize();
    }
}

void Timer::stop()
{
    _running = false;
    _thread.join();
}

bool Timer::running() const
{
    return _running;
}

void Timer::setSingleShot(bool singleShot)
{
    if (this->running() == true)
        return;
    
    _isSingleShot = singleShot;
}

bool Timer::isSingleShot() const
{
    return _isSingleShot;
}

void Timer::setInterval(const Timer::Interval &interval)
{
    if (this->running() == true)
        return;
    
    _interval = interval;
}

const Timer::Interval &Timer::interval() const
{
    return _interval;
}

void Timer::setTimeout(const Timeout &timeout)
{
    if (this->running() == true)
        return;
    
    _timeout = timeout;
}

const Timer::Timeout &Timer::timeout() const
{
    return _timeout;
}

void Timer::_temporize()
{
    if (_isSingleShot == true) {
        this->_sleepThenTimeout();
    }
    else {
        while (this->running() == true) {
            this->_sleepThenTimeout();
        }
    }
}

void Timer::_sleepThenTimeout()
{
    std::this_thread::sleep_for(_interval);
    
    if (this->running() == true)
        this->timeout()();
}

map<char, int> inventory;       // Warehouse with items
mutex m;                        // Mutext for order threads sync
void generateOrder();           // Function for generating an order
void printInventory();          // Print the current state of the Warehouse

int main(int argc, const char * argv[]) {
    
    // set up the initial state of the Warehouse
    inventory.insert(pair<char, int>('A', 150));
    inventory.insert(pair<char, int>('B', 150));
    inventory.insert(pair<char, int>('C', 100));
    inventory.insert(pair<char, int>('D', 100));
    inventory.insert(pair<char, int>('E', 200));
    
    // First order's thread. Initiating new order every 0.5 second
    Timer tOrderThread1([]() {
        generateOrder();
    });
    tOrderThread1.setSingleShot(false);
    tOrderThread1.setInterval(Timer::Interval(500));
    tOrderThread1.start(true);
    
    // Second order's thread. Initiating new order every 0.75 second
    Timer tOrderThread2([]() {
        generateOrder();
    });
    tOrderThread2.setSingleShot(false);
    tOrderThread2.setInterval(Timer::Interval(750));
    tOrderThread2.start(true);
    
    // First order's thread. Initiating new order every 1 second
    Timer tOrderThread3([]() {
        generateOrder();
    });
    tOrderThread3.setSingleShot(false);
    tOrderThread3.setInterval(Timer::Interval(1000));
    tOrderThread3.start(true);
    
    // Thread for maintaining and stopping orders' threads
    Timer tStopOrders([&]() {
        tOrderThread1.stop();
        tOrderThread2.stop();
        tOrderThread3.stop();
    });
    tStopOrders.setSingleShot(true);
    tStopOrders.setInterval(Timer::Interval(10000));
    tStopOrders.start();
    
    return 0;
}

void generateOrder() {
    m.lock();
    int aQuantity = rand() % 10;
    int bQuantity = rand() % 10;
    int cQuantity = rand() % 10;
    int dQuantity = rand() % 10;
    int eQuantity = rand() % 10;
    printf("Generated order: A:%d\tB:%d\tC:%d\tD:%d\tE:%d\n", aQuantity, bQuantity, cQuantity, dQuantity, eQuantity);
    if ((inventory['A'] - aQuantity) > 0 && (inventory['B'] - bQuantity) > 0 && (inventory['C'] - cQuantity) > 0 && (inventory['D'] - dQuantity) > 0 && (inventory['E'] - eQuantity) > 0) {
        inventory['A'] -= aQuantity;
        inventory['B'] -= bQuantity;
        inventory['C'] -= cQuantity;
        inventory['D'] -= dQuantity;
        inventory['E'] -= eQuantity;
        printf("Order shipped successfully!\n");
    }
    else {
        printf("Unable to ship the order!\n");
    }
    printInventory();
    m.unlock();
}

void printInventory() {
    printf("Inventory state: A:%d\tB:%d\tC:%d\tD:%d\tE:%d\n", inventory['A'], inventory['B'], inventory['C'], inventory['D'], inventory['E']);
}

/*
 Initial requirements and notes
 Please make sure that your code will run under either Python 2.6.6 or Python 3.5.1.
 Please post your code and output to a repository on github or bitbucket and share the repository.
 
 
 ------------------------------------------------------
 
 The object of the exercise is to show off your coding style and skill.
 
 Initial conditions:
 Initially, the system contains inventory of
 A x 150
 B x 150
 C x 100
 D x 100
 E x 200
 
 Initially, the system contains no orders
 
 Data source:
 There should be a data source capable of generating one or more streams of orders.
 An order consists of a unique identifier (per stream) we will call the "header", and a demand for between zero and five units each of A,B,C,D, and E, except that there must be at least one unit demanded.
 A valid order (in whatever format you choose): {"Header": 1, "Lines": {"Product": "A", "Quantity": "1"},{"Product": "C", "Quantity": "4"}}
 An invalid order: {"Header": 1, "Lines": {"Product": "B", "Quantity": "0"}}
 Another invalid order: {"Header": 1, "Lines": {"Product": "D", "Quantity": "6"}}
 Feel free to identify streams as you'd like.
 
 Inventory allocator:
 There should be an inventory allocator which allocates inventory to the inbound data according to the following rules:
 1) Inbound orders to the allocator should be individually identifyable (ie two streams may generate orders with an identical header, but these orders should be identifyable from their streams)
 2) Inventory should be allocated on a first come, first served basis; once allocated, inventory is not available to any other order.
 3) Inventory should never drop below 0.
 4) If a line cannot be satisfied, it should not be allocated.  Rather, it should be  backordered (but other lines on the same order may still be satisfied).
 5) When all inventory is zero, the system should halt and produce output listing, in the order received by the system, the header of each order, the quantity on each line, the quantity allocated to each line, and the quantity backordered for each line.
 For instance:
 If the initial conditions are:
 A x 2
 B x 3
 C x 1
 D x 0
 E x 0
 
 And the input is:
 {"Header": 1, "Lines": {"Product": "A", "Quantity": "1"}{"Product": "C", "Quantity": "1"}}
 {"Header": 2, "Lines": {"Product": "E", "Quantity": "5"}}
 {"Header": 3, "Lines": {"Product": "D", "Quantity": "4"}}
 {"Header": 4, "Lines": {"Product": "A", "Quantity": "1"}{"Product": "C", "Quantity": "1"}}
 {"Header": 5, "Lines": {"Product": "B", "Quantity": "3"}}
 {"Header": 6, "Lines": {"Product": "D", "Quantity": "4"}}
 
 The output should be (in whatever format you choose):
 1: 1,0,1,0,0::1,0,1,0,0::0,0,0,0,0
 2: 0,0,0,0,5::0,0,0,0,0::0,0,0,0,5
 3: 0,0,0,4,0::0,0,0,0,0::0,0,0,4,0
 4: 1,0,1,0,0::1,0,0,0,0::0,0,1,0,0
 5: 0,3,0,0,0::0,3,0,0,0::0,0,0,0,0
 
 */
