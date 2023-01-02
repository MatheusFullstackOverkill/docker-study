import React, { useEffect } from 'react'

export default function Index() {

  useEffect(() => {
    fetch(process.env.NEXT_PUBLIC_API_HOST+'/user');
  },[])

  return (
    <div>Teste</div>
  )
}
