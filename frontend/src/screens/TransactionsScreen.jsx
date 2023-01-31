import React from 'react';
import TransactionsList from './TransactionsList';

const TransactionsScreen = () => {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch('http://localhost:8000/api/transactions/');
      const data = await response.json();
      setTransactions(data);
    };

    fetchData();
  }, []);

  return (
    <div>
      <TransactionsList transactions={transactions} />
    </div>
  );
};

export default TransactionsScreen;