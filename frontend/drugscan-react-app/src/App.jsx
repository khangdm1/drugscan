import DrugList from './components/DrugList'
import DrugForm from './components/DrugForm'
import DrugUpload from './components/DrugUpload'
import { useState } from 'react'

function App() {
	const [refreshFlag, setRefreshFlag] = useState(0)

	const triggerRefresh = () => setRefreshFlag((f) => f + 1)

	return (
		<div
			style={{
				display: 'flex',
				padding: '2rem',
				gap: '2rem',
				fontFamily: 'Arial, sans-serif',
			}}
		>
			<div
				style={{
					flex: '0 0 300px',
					display: 'flex',
					flexDirection: 'column',
					gap: '1.5rem',
				}}
			>
				<h2>🔍 Tác vụ</h2>
				<DrugForm onAdded={triggerRefresh} />
				<DrugUpload onUploaded={triggerRefresh} />
			</div>

			<div style={{ flex: 1 }}>
				<DrugList refreshFlag={refreshFlag} />
			</div>
		</div>
	)
}

export default App
